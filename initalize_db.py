# -*- coding:utf-8 -*-
from datetime import date, time, datetime
from app import db
from app.models import Category, Tag, Post

db.create_all()

category = Category('python')
# tag1 = Tag('flask')
tag1 = Tag.query.filter(Tag.name == 'flask').first()
# tag2 = Tag('web framework')
tag2 = Tag.query.filter(Tag.name == 'web framework').first()
post1 = Post('Baseline Pattern, Coaching Pattern Series', 'flask is a micro-web framework', category, [tag1, tag2])
# post2 = Post('What is flask-2', 'flask is a micro-web framework', category, [tag1, tag2])
# post3 = Post('What is flask-3', 'flask is a micro-web framework', category, [tag1])

db.session.add(category)
db.session.add(tag1)
db.session.add(tag2)
db.session.add(post1)
# db.session.add(post2)
# db.session.add(post3)
db.session.commit()