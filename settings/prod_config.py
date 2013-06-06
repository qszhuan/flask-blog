# -*- coding:utf-8 -*-
import os

# csrf settings
CSRF_ENABLED = True
SECRET_KEY = 'development secret key'
DEBUG = True
basedir = os.path.abspath(os.path.dirname(__file__))
print basedir

#database settings
DATABASE_PATH = os.path.abspath(os.path.join(basedir, os.pardir))

if os.environ.get('DATABASE_URL') is None:
    SQLALCHEMY_DATABASE_URI = os.path.join('postgresql://localhost', 'blog')
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
else:
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    DEBUG = False

# mail server settings
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587
MAIL_USERNAME = 'birdchn@gmail.com'
MAIL_PASSWORD = '12345!@#$'
MAIL_USE_TLS = True

# blog settings
BLOG_PATH = os.path.abspath(os.path.join(basedir, os.pardir, 'blog'))
TEMP_BLOG_PATH = os.path.abspath(os.path.join(basedir, os.pardir, 'blog_tmp'))

# templates settings
TEMPLATE_DIR = os.path.join(os.path.join(basedir, os.pardir, 'app', 'templates'))


