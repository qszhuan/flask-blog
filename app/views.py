# -*- coding:utf-8 -*-
import codecs

import os
from flask import render_template, Session
from jinja2 import Markup
import markdown
from sqlalchemy import func
from app import app, db
from app.models import Post, Category, Tag

sample = u"""
> 给出一些例子代码：
>
>     return shell_exec("echo $input | $markdown_script");
*   Red
*   Green
*   Blue
[id]: http://example.com/  "Optional Title Here"
[a]: http://www.baidu.com 'fdsf'

Use the `printf()` function.
"""


@app.route('/about')
def about():
    template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
    about_file = os.path.join(template_dir, 'about.md')
    with codecs.open(about_file, mode='r', encoding='utf-8') as f:
        text = f.read()
        content = Markup(markdown.markdown(text))
        return render_template('about.html', content=content)


@app.route('/')
def index():
    categories = Category.query.all()
    tags = Tag.query.all()
    func_strftime = func.strftime("%m-%Y", Post.publish_date)
    archives = db.session.query(func_strftime, func.count(Post.id)).group_by(func_strftime).all()
    recent_posts = Post.query.order_by(Post.publish_date.desc()).limit(5)
    content = Markup(markdown.markdown(sample))
    return render_template('index.html', **locals())
