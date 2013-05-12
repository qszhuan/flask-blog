##BeautifulSoup的使用
Category: python
Tags: BeautifulSoup urlopen ted subtitle


<pre><code class="python">
from urllib2 import urlopen
from BeautifulSoup import BeautifulSoup
import sys


def main():
    if 2 > len(sys.argv):
        print 'python {0:s} <ted_url>'.format(__file__)
        return

    url = sys.argv[1]
    soup = BeautifulSoup(urlopen(url).read())
    attr_map = soup.find(id="share_and_save").attrMap
    langs = ['en', 'zh-cn']
    for lang in langs:
        subtitle_url = 'http://www.ted.com/talks/subtitles/id/%s/lang/%s/format/html' % (attr_map['data-id'], lang)
        subtitle = BeautifulSoup(urlopen(subtitle_url).read()).text.encode('utf-8')
        with open("%s-%s.txt" % ((attr_map['data-title']), lang), 'w') as f:
            f.write(subtitle)
if __name__ == '__main__':
    main()
</code></pre>


