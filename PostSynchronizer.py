# -*- coding:utf-8 -*-
import os
from app import db, app
from app.PostGenerator import PostGenerator


class PostSynchronizer(object):
    def init_db(self):
        self.drop()
        db.create_all()

    def drop(self):
        db.session.remove()
        db.drop_all()

    def sync_blog_into_db(self, file):
        post = PostGenerator().generate(file)
        self._sync_post(post)
        return post

    def _sync_post(self, post):
        db.session.add(post)
        db.session.commit()


if __name__ == '__main__':
    synchronizer = PostSynchronizer()
    synchronizer.init_db()
    blog_dir = app.config['BLOG_PATH']

    for r, d, f in os.walk(blog_dir):
        print r, d, f
        for file in f:
            if file.endswith(".md"):
                synchronizer.sync_blog_into_db(os.path.join(r, file))
