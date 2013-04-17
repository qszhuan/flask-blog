# -*- coding:utf-8 -*-
import codecs

import os
from flask import render_template
from jinja2 import Markup
import markdown
from app import app

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
    content = Markup(markdown.markdown(sample))
    return render_template('index.html', **locals())
