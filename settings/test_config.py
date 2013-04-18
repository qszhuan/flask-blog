# -*- coding:utf-8 -*-
import os

#testing
TESTING = True

# csrf settings
CSRF_ENABLED = False
SECRET_KEY = 'test secret key'

basedir = os.path.abspath('..')

#database settings
DATABASE_PATH = os.path.abspath(os.path.join(basedir, os.pardir))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(DATABASE_PATH, 'test.db')

# mail server settings
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587
MAIL_USERNAME = 'birdchn@gmail.com'
MAIL_PASSWORD = '12345!@#$'
MAIL_USE_TLS = True

