# -*- coding:utf-8 -*-
from sqlalchemy import func
from app import db
from app.models import Category, Tag, Post
from TestBase import TestBase


class PostTest(TestBase):

    def test_should_create_post(self):
        category = Category('python')
        tag1 = Tag('flask')
        tag2 = Tag('web framework')
        post1 = Post('What is flask-1', 'flask is a micro-web framework', category, [tag1, tag2])
        post2 = Post('What is flask-2', 'flask is a micro-web framework', category, [tag1, tag2])
        post3 = Post('What is flask-3', 'flask is a micro-web framework', category, [tag1])

        db.session.add(category)
        db.session.add(tag1)
        db.session.add(tag2)
        db.session.add(post1)
        db.session.add(post2)
        db.session.add(post3)
        db.session.commit()

        self.assertEqual(post1.category, category)
        self.assertItemsEqual(post1.tags, [tag1, tag2])
        self.assertItemsEqual(category.posts.all(), [post1, post2, post3])
        self.assertItemsEqual(tag1.posts.all(), [post1, post2, post3])

