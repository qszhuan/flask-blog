##Mac 工具  
Category: mac
Tags: Homebrew, iterm2, autojump, oh-my-zsh   
Date: 2013-04-26
 
 
####[Homebrew][homebrew]
Mac OS 下的软件包管理工具，安装非常简单:  

	ruby -e "$(curl -fsSL https://raw.github.com/mxcl/homebrew/go)"

安装 `autojump`:  
	
	brew install autojump
查看 `autojump`安装信息：


	➜  Documents  brew info autojump
	autojump: stable 21.4.2, HEAD
	https://github.com/joelthelion/autojump#name
	/usr/local/Cellar/autojump/21.4.2 (10 files, 96K) *
  		Built from source
	https://github.com/mxcl/homebrew/commits/master/Library/Formula/autojump.rb
	==> Caveats
	Add the following line to your ~/.bash_profile or ~/.zshrc file (and remember
	to source the file to update your current session):
	
	[[ -s `brew --prefix`/etc/autojump.sh ]] && . `brew --prefix`/etc/autojump.sh


[homebrew]: http://mxcl.github.io/homebrew/

####[iTerm2][iterm2]
iterm2是mac自带终端的很好的替代品。  
![image][iterm2]

####文本选择：
有两种模式，均为选中即复制:  

* 鼠标选择： 用鼠标选择文本后，文本自动复制到剪贴板。
* 非鼠标选择：`command ＋ f` 找到匹配文字，如果有多个匹配，`command + G`选择下一个匹配，`command + shift + G`选择上一个匹配，找到后按`tab`键会自动选中单词，可重复按`tab`键向后进行整词选择。


####面板分割:
* `command + d`: 垂直分割
* `command + shift + d`: 水平分割
* `command + [` 或者 `command + ]`：在面板间切换

####自动完成
`command + ;`: 能够调出最近使用的命令，如果键入`m`后再按`command + ;`，会列出当前目录下以m开头的文件和文件夹名，之前输入过的m开头的命令。

####剪贴板历史
`command + shift + h`： 列出剪贴板的历史。

####切换全屏
`command + enter`: 切换全屏。

[iterm2]: http://www.iterm2.com/images/logo.png



####[autojump][autojump]
自动记录用户访问的目录，然后键入`j + <部分目录名>`，便会进入相应目录中。

`autojump -s`可以看到所有保存的目录：

 
	➜  Documents  autojump -s
	10.0:	/Users/TWIS/.oh-my-zsh
	10.0:	/Users/TWIS/.oh-my-zsh/plugins
	14.1:	/Users/TWIS/Desktop
	30.0:	/Users/TWIS/Downloads
	31.6:	/Users/TWIS/Documents
	Total key weight: 95. Number of stored dirs: 5


[autojump]: https://github.com/joelthelion/autojump/wiki


####[oh-my-zsh](https://github.com/robbyrussell/oh-my-zsh)
oh-my-zsh是基于zsh的功能做了一个扩展，方便的插件管理、主题自定义，以及漂亮的自动完成效果。

