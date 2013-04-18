Basic grammar of markdown
Category: markdown
tags: markdown


This is an H1
=============
This is an H2
-------------
# 这是 H1

## 这是 H2
###### 这是 H6
** hello **

+   Red
+   Green
+   Blue

1.  Bird
1.  McHale
1.  Parish


>
This is a blockquote with two paragraphs. Lorem ipsum dolor sit amet,
> consectetuer adipiscing elit. Aliquam hendrerit mi posuere lectus.
> Vestibulum enim wisi, viverra nec, fringilla in, laoreet vitae, risus.
>
> Donec sit amet nisl. Aliquam semper ipsum sit amet velit. Suspendisse
> id sem consectetuer libero luctus adipiscing.
> This is a blockquote with two paragraphs. Lorem ipsum dolor sit amet,
consectetuer adipiscing elit. Aliquam hendrerit mi posuere lectus.
Vestibulum enim wisi, viverra nec, fringilla in, laoreet vitae, risus.

> >Donec sit amet nisl. Aliquam semper ipsum sit amet velit. Suspendisse
id sem consectetuer libero luctus adipiscing.

>>
> ## 这是一个标题。
> >
> 1.   这是第一行列表项。
> 2.   这是第二行列表项。
>
> 给出一些例子代码：
>
>     return shell_exec("echo $input | $markdown_script");



*   Red
*   Green
*   Blue

3. Bird
1. McHale
8. Parish


* Lorem ipsum dolor sit amet, consectetuer adipiscing elit.
 Aliquam hendrerit mi posuere lectus. Vestibulum enim wisi,
    viverra nec, fringilla in, laoreet vitae, risus.
*   Donec sit amet nisl. Aliquam semper ipsum sit amet velit.
    Suspendisse id sem consectetuer libero luctus adipiscing.


*   Bird
*   Magic

Here is an example of AppleScript:

    tell application "Foo"
        beep
    end tell

    print "a"

---------------------------------------
* * *

***

*****

- - -


First Header | Second Header | Third Header
:----------- | :-----------: | -----------:
Left         | Center        | Right
Left         | Center        | Right



This is [an example](http://example.com/ "Title") inline link.

This is [an example] [id] reference-style link.

[link text][a]
[link text][A]

[id]: http://example.com/  "Optional Title Here"
[a]: http://www.baidu.com 'fdsf'

*single asterisks*

_single underscores_

**double asterisks**

__double underscores__

un*frigging*believable

\*this text is surrounded by literal asterisks\*


Use the `printf()` function.
