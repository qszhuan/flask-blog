# -*- coding:utf-8 -*-
from unittest import TestCase
from pygments.lexers import guess_lexer
from pygments.lexers.math import NumPyLexer


class Jinja2ExTest(TestCase):
    def test_should_guess_correct_lexer_for_python_code(self):
        code_sniffer = '#!/usr/bin/python\n' \
                       'print "Hello World!"'
        lexer = guess_lexer(code_sniffer)
        self.assertTrue(isinstance(lexer, NumPyLexer))

    def test_should_guess_correct_lexer_for_python_code2(self):
        code_sniffer = """import os
import sys

os.path.join('.', 'test.py')
"""
        lexer = guess_lexer(code_sniffer)
        # self.assertTrue(isinstance(lexer, NumPyLexer))
