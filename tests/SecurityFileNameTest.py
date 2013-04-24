# -*- coding:utf-8 -*-
from unittest import TestCase
from werkzeug.utils import secure_filename


class SecurityFileNameTest(TestCase):

    def test_should_get_security_file_name(self):
        filename = secure_filename("a b c")
        self.assertEqual("a_b_c", filename)

        filename = secure_filename("a - b c")
        self.assertEqual("a_-_b_c", filename)

        filename = secure_filename("a _ b c")
        self.assertEqual("a___b_c", filename)

        filename = secure_filename("markdown的使用")
        self.assertEqual("markdown", filename)
