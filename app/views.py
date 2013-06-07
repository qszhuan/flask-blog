# -*- coding:utf-8 -*-
import codecs
import os
import random
from shutil import move
from flask import render_template, request, redirect, url_for
from jinja2 import Markup
import markdown
from sqlalchemy import func, extract
from PostSynchronizer import PostSynchronizer
from app import app, db
from app.PostGenerator import PostGenerator
from app.models import Post, Category, Tag


def avatar():
    return 'http://www.gravatar.com/avatar/' + "aecf6efff2be54fdf7f8c7373acf0b5a" + '?d=mm&s=' + str(280)


@app.route('/about')
def about():
    me = avatar()
    about_file = os.path.join(app.config["TEMPLATE_DIR"], 'about.md')
    name = 'Qingshan Zhuan'
    desc = 'Developer, Consultant. Working at ThoughtWorks'
    email = u'http://www.google.com/recaptcha/mailhide/d?k\07501GF3Ml8jmtbv43VhhfYErOA\75\75\46c\75mU5fCywLel1JB5b3nDCyRyz2QQvCANeWakKiD0ABlEE\075'

    with codecs.open(about_file, mode='r', encoding='utf-8') as f:
        content = Markup(markdown.markdown(f.read()))
        return render_template('about.html', **locals())


@app.route('/')
def index():
    return render_template('index.html', **_contents())


@app.route('/blog/<blog_title>')
def blog(blog_title):
    post = Post.query.filter(Post.title == blog_title).first()
    return render_template('blog.html', post=post, **_contents())


@app.route('/category/<category_name>')
def category(category_name):
    posts = db.session.query(Post).join(Post.category).filter(Category.name == category_name).order_by(
        Post.publish_date.desc())
    locals().update(_contents())
    return render_template('category.html', **locals())


@app.route('/tag/<tag_name>')
def tag(tag_name):
    posts = db.session.query(Post).join(Post.tags).filter(Tag.name == tag_name).order_by(Post.publish_date.desc())
    return render_template('tag.html', **dict(locals(), **_contents()))


@app.route('/archive/<year>/<month>')
def archive(year, month):
    posts = Post.query.filter(
        extract('year', Post.publish_date) == year, extract('month', Post.publish_date) == float(month)).order_by(
        Post.publish_date.desc())
    return render_template('archive.html', **dict(locals(), **_contents()))


@app.route('/blog_radar')
def blog_radar():
    return render_template('blog_radar.html')


@app.route('/timeline')
def timeline():
    return render_template('timeline.html')


@app.route('/books')
def books():
    return render_template('books.html')


@app.route('/upload')
def upload():
    pass


@app.route('/up', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files.get('file')
        if file and allowed_file(file.filename):
            file_name = os.path.join(app.config["TEMP_BLOG_PATH"], file.filename)
            file.save(file_name)
            post = PostGenerator().generate(file_name)
            return render_template('upload_file.html', post=post, filename=file.filename)

    return render_template('upload_file.html')


@app.route('/post/<filename>')
def post(filename):
    src = os.path.join(app.config["TEMP_BLOG_PATH"], filename)
    dst = os.path.join(app.config["BLOG_PATH"], filename)
    move(src, dst)
    post = PostSynchronizer().sync_blog_into_db(dst)
    return redirect(url_for('blog', blog_title=post.title))


ALLOWED_EXTENSIONS = {'md', 'txt'}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[-1] in ALLOWED_EXTENSIONS


def _contents():
    categories = Category.query.all()
    query = db.session.query(Tag, db.func.count(Post.id)).join(Post.tags).group_by(Tag.id).order_by(
        db.desc(db.func.count(Post.id)))
    tags = query.all()
    year_func = extract('year', Post.publish_date)
    month_func = extract('month', Post.publish_date)
    archives = db.session.query(year_func, month_func, func.count(Post.id)).group_by(year_func).group_by(
        month_func).all()
    recent_posts = Post.query.order_by(Post.publish_date.desc()).limit(5)
    return {'categories': categories, 'tags': tags, 'archives': archives, 'recent_posts': recent_posts}
