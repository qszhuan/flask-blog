# -*- coding:utf-8 -*-
import codecs
from datetime import datetime
import string
from app.models import Category, Tag, Post

DATE_FORMAT = '%Y-%m-%d'
MISSING = 'MISSING'
MARKDOWN_H2 = '##'
CATEGORY_PREFIX = 'Category:'
TAG_PREFIX = 'Tags:'
PUBLISH_DATE_PREFIX = 'Date:'


class PostGenerator(object):
    def generate(self, file):
        with codecs.open(file, mode='r', encoding='utf-8') as f:
            contents = f.readlines()
            title = contents[0].lstrip(MARKDOWN_H2) if contents[0].startswith(MARKDOWN_H2) else MISSING

            category_name = contents[1].lstrip(CATEGORY_PREFIX).strip() if contents[1].startswith(
                CATEGORY_PREFIX) else MISSING
            category = self._generate_category(category_name)

            tag_names = contents[2].lstrip(TAG_PREFIX) if contents[2].startswith(TAG_PREFIX) else MISSING
            tag_names = [each.strip() for each in tag_names.split(',')]
            tags = self._generate_tags(tag_names)

            create_date = contents[3].lstrip(PUBLISH_DATE_PREFIX).strip() if contents[
                3].startswith(PUBLISH_DATE_PREFIX) else MISSING
            body_cursor = 0
            if title != MISSING:
                body_cursor = 1
            if category_name != MISSING:
                body_cursor += 1
            if tag_names[0] != MISSING:
                body_cursor += 1
            if create_date != MISSING:
                body_cursor += 1

            body = ''.join(contents[body_cursor:])

            try:
                create_date = datetime.strptime(create_date, DATE_FORMAT)
            except:
                create_date = datetime.utcnow()

            post = self._generate_post(title, body, category, tags, create_date)
            return post

    def _generate_category(self, category_name):
        return Category.query.filter(Category.name == category_name).first() or Category(category_name)

    def _generate_tags(self, tag_names):
        for tag_name in tag_names:
            tag = Tag.query.filter(Tag.name == tag_name).first() or Tag(tag_name)
            yield tag

    def _generate_post(self, title, body, category, tags, create_date):
        post = Post(title=title, body=body, category=category, tags=list(tags), publish_date=create_date)
        return post


