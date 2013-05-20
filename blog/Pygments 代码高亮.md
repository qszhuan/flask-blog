##Pygments 代码高亮  
Category: python  
Tags: python, pygments, lexer, highlight, pygmentize, markdown
Date: 2013-04-26



[Pygments][pygments]是一个基于python的代码语法高亮库。其支持的语言相当的广，而且你也可以轻松地对它进行扩展。

Pygments由四个组件实现代码的语法高亮:

* **Lexer（词法分析器）** Lexer把代码分割为token。token是具有类型的代码片段，可以决定文本的语义表示（例如，关键字，字符串或注释）。每一种语言或者文本标记格式，Pygments都有相应的Lexer。
* **Filter（过滤器）** token可以以流的形式通过Filter管道。Filter通常用来修改token类型或者文本，例如大写所有关键字。
* **Formatter（格式器）** 然后，Formatter把token流以HTML、LaTeX或这RTF的格式输出到文件。
* **Style（样式）** 在token流输出时，style决定了怎样高亮所有不同的token类型。它把token类型和属性关联起来，如设置字体为<span style="color:red">**红色并加粗**</span>。

<br>
下面这段代码是我为本博客写的[jinja2][jinja2]模板的filter扩展, 功能就是在页面显示之前做语法高亮。

<pre><code class="python">
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
        lexer = get_lexer_by_name(block.code['class']) if block.code.has_key('class') else guess_lexer(block.text)
        try:
            code = ''.join([unicode(item.text) for item in block.contents])
            formatter = HtmlFormatter(linenos='inline', linenostart=0, full=True)
            code_hl = pygments.highlight(code, lexer, formatter)
            block.contents = [BeautifulSoup(code_hl)]
            block.name = 'div'
        except:
            raise
    return Markup(soup)</code></pre>

markdown语法中会将代码段在转换成HTML时将代码段嵌入到`<pre><code></code></pre>`中，然后我们
所需要做的就是解析生成的html，将其中的代码段进行语法高亮。

<br>
在`for`语句中的第一行有两个方法：`get_lexer_by_name`和`guess_lexer`。

因为默认生成的html标签中没有标明源码的编程语言，所以要进行语法高亮就必须根据源代码猜出这是那种语言写的代码，`guess_lexer`就是干这个用的。不过，在我实验时，它总是猜不对，即使我用其官网上的例子也是如此，不知道是什么原因。

多亏了`Markdown`语法是完全兼容`HTML`的。在HTML区块标签间的Markdown格式语法将不会被处理。这样我们就可以手动加上编程语言的属性，也就是`<pre><code class="python"></code></pre>`。

这样，我们就可以通过`get_lexer_by_name`方法来定位到正确的Lexer了。

<br>
然后，把所有的代码段通过`HTMLFormatter`进行格式化。`HTMLFormatter`构造函数中可以传入很多参数，我们这里用到了三个：

`linenos`用来设置行号，默认为`False`，还可以设置成`inline`（代码和行号显示在一个块中）和`table`(代码和行号分别显示为table的两列)。

`linenostart`用来设置起始行号，默认为`1`, 貌似设为零更有感觉。

最后一个参数`full`，当置为`True`时，会转换成一个"完整"的HTML文档。

这里没有用到filter，因为暂时没想到这方面的需求，以后再看看。

<br>
万事俱备，该祭出最终的函数`pygments.highlight`了，很明显，用它组合前面提到的代码段，lexer和formatter来生成高亮后的文档。

<br>
其实，还没有完。

上面这一部分Pygments做的是找出代码段，并把需要高亮的token加上了特定的HTML标签和属性，还需要配合合适的CSS才行。当`HTMLFormatter`创建时传入`full=True`会把生成的整个文档插入到博客中，其中包括了CSS样式。

但这并不是我们想要的，为了让代码和生成出来的HTML文档更干净，更易于维护，我们先把生成的CSS拷贝到新的CSS文件中并应用到当前文档中，然后把HTMLFormatter部分修改为`HtmlFormatter(linenos='inline', linenostart=0 `<strike>`, full=True`</strike>`)`。

其实，css可以完全使用`pygmentize`命令行工具来生成：  
`pygmentize -S default -f html > syntax.css`

<br>
很多人在用`Jekyll`在github上写博客，也是可以使用Pygments做语法高亮的哦。还有一个pygments.rb，是用ruby对pygments的包装，这样在ruby中也可以用pygments来做语法高亮了

[jinja2]: http://jinja.pocoo.org/ 
[pygments]: http://pygments.org/
