# -*- coding:utf-8 -*-
from flask.ext.sqlalchemy import SQLAlchemy
from flask import Flask
from settings import prod_config

app = Flask(__name__)
app.config.from_object(prod_config)
db = SQLAlchemy(app)

from flask.ext.babel import Babel
babel = Babel(app)

from app import views, models

