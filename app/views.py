# -*- coding:utf-8 -*-
import codecs
import os
from flask import render_template
from jinja2 import Markup
import markdown
from sqlalchemy import func
from app import app, db
from app.models import Post, Category, Tag


def avatar():
    return 'http://www.gravatar.com/avatar/' + "aecf6efff2be54fdf7f8c7373acf0b5a" + '?d=mm&s=' + str(280)


@app.route('/about')
def about():
    me = avatar()
    about_file = os.path.join(app.config["TEMPLATE_DIR"], 'about.md')
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
    posts = Category.query.filter(Category.name == category_name).first().posts
    locals().update(_contents())
    return render_template('category.html', **locals())


@app.route('/tag/<tag_name>')
def tag(tag_name):
    posts = Tag.query.filter(Tag.name == tag_name).first().posts
    return render_template('tag.html', **dict(locals(), **_contents()))


@app.route('/archive/<archive_period>')
def archive(archive_period):
    posts = Post.query.filter(func.strftime("%m-%Y", Post.publish_date) == archive_period)
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


def _contents():
    categories = Category.query.all()
    tags = Tag.query.all()
    func_strftime = func.strftime("%m-%Y", Post.publish_date)
    archives = db.session.query(func_strftime, func.count(Post.id)).group_by(func_strftime).all()
    recent_posts = Post.query.order_by(Post.publish_date.desc()).limit(5)
    return locals()   # {'categories': categories, 'tags': tags, 'archives': archives, 'recent_posts': recent_posts}
