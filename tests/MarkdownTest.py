# -*- coding:utf-8 -*-
from unittest import TestCase
import markdown


class MarkdownTest(TestCase):
    def test_for_code(self):
        md = '    print "hello"'

        expected = u'''<pre><code>print "hello"\n</code></pre>'''
        html = markdown.markdown(md)
        self.assertEqual(expected, html)

    def test_should_not_transform_html(self):
        md = '<pre code="python">print "hello"</pre>'
        expected = '<pre code="python">print "hello"</pre>'
        html = markdown.markdown(md)
        self.assertEqual(expected, html)

    def test_should_not_tranform_html_even_have_tab_space_in_start_of_line(self):
        md = '''<pre code="python">
def fun():
    a = "a"

    b = "b"

    </pre>'''
        expected = '''<pre code="python">
def fun():
    a = "a"

    b = "b"

    </pre>'''
        html = markdown.markdown(md)
        self.assertEqual(expected, html)
