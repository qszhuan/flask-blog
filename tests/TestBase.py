# -*- coding:utf-8 -*-
import unittest
from app import app, db
from settings import test_config


class TestBase(unittest.TestCase):
    def setUp(self):
        app.config.from_object(test_config)
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
