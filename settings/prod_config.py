# -*- coding:utf-8 -*-
import os

# csrf settings
CSRF_ENABLED = True
SECRET_KEY = 'development secret key'

basedir = os.path.abspath(os.path.dirname(__file__))
basedir = os.path.abspath('..')

#database settings
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')

# mail server settings
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587
MAIL_USERNAME = 'birdchn@gmail.com'
MAIL_PASSWORD = '12345!@#$'
MAIL_USE_TLS = True

