# -*- coding:utf-8 -*-
import codecs
from app.models import Category, Tag, Post


class PostGenerator(object):

    def generate(self, file):
        with codecs.open(file, mode='r', encoding='utf-8') as f:
            title = f.readline().strip()
            category_name = f.readline().split()[-1]
            category = self._generate_category(category_name)
            tag_names = f.readline().split()[1:]
            tags = self._generate_tags(tag_names)
            body = ''.join([f.read(), f.read()])

            post = self._generate_post(title, body, category, tags)
            return post

    def _generate_category(self, category_name):
        return Category.query.filter(Category.name == category_name).first() or Category(category_name)

    def _generate_tags(self, tag_names):
        for tag_name in tag_names:
            tag = Tag.query.filter(Tag.name == tag_name).first() or Tag(tag_name)
            yield tag

    def _generate_post(self, title, body, category, tags):
        post = Post(title, body, category, list(tags))
        return post


