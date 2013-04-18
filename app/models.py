# -*- coding:utf-8 -*-
from datetime import datetime
from app import db


tags = db.Table('tags',
                db.Column('tag_id', db.Integer, db.ForeignKey('tag.id')),
                db.Column('post_id', db.Integer, db.ForeignKey('post.id'))
                )


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Tag %r>' % self.name


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "<Category %r>" % self.name


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256))
    body = db.Column(db.Text(1024))
    publish_date = db.Column(db.DateTime)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))

    category = db.relationship('Category', backref=db.backref('posts'))
    tags = db.relationship('Tag', secondary=tags, backref=db.backref('posts'))

    def __init__(self, title, body, category, tags, publish_date=None):
        self.title = title
        self.body = body
        self.category = category
        self.publish_date = publish_date or datetime.utcnow()
        self.tags = tags

    def __repr__(self):
        return '<Post %r>' % self.title



