# -*- coding: utf-8 -*-
from jinja2 import Markup
from markdown import markdown


def markup(text, *args, **kwargs):
    return Markup(markdown(text, *args, **kwargs))