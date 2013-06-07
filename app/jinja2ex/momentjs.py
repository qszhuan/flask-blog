from datetime import date
from jinja2 import Markup


class momentjs:
    def __init__(self, date1=None, **kwargs):
        if date1:
            self.date = date1
        else:
            year = int(kwargs.get('year', 1970))
            month = int(kwargs.get('month', 1))
            day = int(kwargs.get('day', 1))
            self.date = date(year, month, day)

    def render(self, format):
        return Markup('<script>\ndocument.write(moment("%s").%s);\n</script>' % (
            self.date.strftime('%Y-%m-%dT%H:%M:%S Z'), format))

    def format(self, fmt):
        return self.render('format("%s")' % fmt)

    def calendar(self):
        return self.render('calendar()')

    def fromNow(self):
        return self.render('fromNow()')

