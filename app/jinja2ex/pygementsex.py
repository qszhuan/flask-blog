# -*- coding:utf-8 -*-
from BeautifulSoup import BeautifulSoup
from jinja2 import Markup
import pygments
from pygments.formatters.html import HtmlFormatter
from pygments.lexers import guess_lexer, get_lexer_by_name


def highlight(html):
    soup = BeautifulSoup(html)
    code_blocks = soup.findAll('pre')
    for block in code_blocks:
        lexer_key = block.code.has_key('class')
        if not lexer_key:
            continue
        lexer = get_lexer_by_name(block.code['class'], stripall=True)
        try:
            code = ''.join([unicode(item.text) for item in block.contents])
            formatter = HtmlFormatter()
            code_hl = pygments.highlight(code, lexer, formatter)
            block.contents = [BeautifulSoup(code_hl)]
            block.name = 'div'
        except:
            raise
    return Markup(soup)