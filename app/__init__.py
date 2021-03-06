# -*- coding:utf-8 -*-
from flask.ext.sqlalchemy import SQLAlchemy
from flask import Flask
from app.jinja2ex.markdownex import markup
from app.jinja2ex.momentjs import momentjs
from app.jinja2ex.pygementsex import highlight
from settings import prod_config

app = Flask(__name__)
app.config.from_object(prod_config)
db = SQLAlchemy(app)
print app.config['SQLALCHEMY_DATABASE_URI']
# db.create_all()

from flask.ext.babel import Babel
babel = Babel(app)

app.jinja_env.filters['markup'] = markup
app.jinja_env.filters['highlight'] = highlight
app.jinja_env.globals['momentjs'] = momentjs

from app import views, models

