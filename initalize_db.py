# -*- coding:utf-8 -*-
import codecs
from datetime import date, time, datetime
import os
from app import db, app
from app.models import Category, Tag, Post


class DBInitializer(object):
    def __init__(self):
        db.create_all()

    def init(self):
        self.drop()
        db.create_all()

    def drop(self):
        db.session.remove()
        db.drop_all()

    def sync_blog_into_db(self, file):
        with codecs.open(file, mode='r', encoding='utf-8') as f:
            title = f.readline()
            category_name = f.readline().split()[-1]
            category = self._sync_category(category_name)
            tag_names = f.readline().split()[1:]
            tags = self._sync_tags(tag_names)
            body = ''.join([f.read(), f.read()])

            self._sync_post(title, body, category, list(tags))

    def _sync_category(self, category_name):
        category = Category.query.filter(Category.name == category_name).first()
        if category is None:
            category = Category(category_name)
            db.session.add(category)
            db.session.commit()
        return category

    def _sync_tags(self, tags):
        for tag_name in tags:
            tag = Tag.query.filter(Tag.name == tag_name).first()
            if tag is None:
                tag = Tag(tag_name)
                db.session.add(tag)
                db.session.commit()
            yield tag

    def _sync_post(self, title, body, category, tags):
        post = Post(title, body, category, tags)
        db.session.add(post)
        db.session.commit()


if __name__ == '__main__':
    db_initializer = DBInitializer()
    db_initializer.init()
    blog_dir = app.config['BLOG_PATH']

    for r, d, f in os.walk(blog_dir):
        print r, d, f
        for file in f:
            if file.endswith(".md"):
                db_initializer.sync_blog_into_db(os.path.join(r, file))
