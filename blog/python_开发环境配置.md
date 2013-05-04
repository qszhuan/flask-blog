##Python 开发环境配置  
Category: python  
Tags: pip, virtualenv, pycharm, ipython  
Date: 2013-05-04




#### [setuptools][setuptools]
>Download, build, install, upgrade, and uninstall Python packages -- easily!

去<https://pypi.python.org/pypi/setuptools>找到合适的蛋。我当前用的是python2.7，所以选择了[setuptools-0.6c11-py2.7.egg][setuptools]。

* 命令行下下载蛋：

		curl -o https://pypi.python.org/packages/2.7/s/setuptools/setuptools-0.6c11-py2.7.egg#md5=fe1f997bc722265116870bc7919059ea

* 安装：


		sudo sh setuptools-0.6c11-py2.7.egg


然后就可以使用`esay_install`命令来安装包了。

[setuptools]: https://pypi.python.org/packages/2.7/s/setuptools/setuptools-0.6c11-py2.7.egg#md5=fe1f997bc722265116870bc7919059ea


#### [pip][pip]
>A tool for installing and managing Python packages.

不要困惑，pip和setuptools都是python的包管理工具，其实setuptools我没用过，只是用它来装pip。会用了pip，就没有动力再去学其他的了。

安装：

	sudo easy_install pip

	
借用官网上的quick start：

* 安装包：

        $ pip install SomePackage==1.0
        [...]
        Successfully installed SomePackage


* 查看安装了那些文件：

        $ pip show --files SomePackage
        Name: SomePackage
        Version: 1.0
        Location: /my/env/lib/pythonx.x/site-packages
        Files:
          ../somepackage/__init__.py
          [...]


* 查看哪些包过期了：

        $ pip list --outdated
              SomePackage (Current: 1.0 Latest: 2.0)

* 更新包

        $ pip install --upgrade SomePackage
              [...]
              Found existing installation: SomePackage 1.0
              Uninstalling SomePackage:
                Successfully uninstalled SomePackage
              Running setup.py install for SomePackage
              Successfully installed SomePackage


* 卸载包

        $ pip uninstall SomePackage
        Uninstalling SomePackage:
            /my/env/lib/pythonx.x/site-packages/somepackage
            Proceed (y/n)? y
        Successfully uninstalled SomePackage


* 查看安装了哪些包

        (flask)➜  ~  pip freeze
        Babel==0.9.6
        BeautifulSoup==3.2.1
        Flask==0.9
        Flask-Babel==0.8
        Flask-Login==0.1.3
        Flask-Mail==0.7.6
        Flask-OpenID==1.1.1
        Flask-SQLAlchemy==0.16
        Flask-Script==0.5.3
        Flask-Uploads==0.1.3
        Flask-WTF==0.8.2
        Flask-WhooshAlchemy==0.55a
        Jinja2==2.6
        Markdown==2.3.1
        Pygments==1.6
        SQLAlchemy==0.7.9

* 从依赖文件安装包

    依赖文件`requirements.txt`格式如下：

        flask=0.9
        ipython
        babel>=0.2
        ...


    安装命令为：

        $ pip install -r requirements.txt


[pip]: https://pypi.python.org/pypi/pip


####[virtualenv][virtualenv]
virtualenv可以用来创建虚拟的，独立的python开发环境，你可以在某一环境安装所需的python库，而不会影响到其他环境。

    $ sudo pip install virtualenv


然后就可以创建虚拟环境了：

    $ virtualenv my_env
    $ . my_env/bin/activate
    (my_env)$ pip install SomePackage

[virtualenv]:http://www.virtualenv.org/en/latest/


####[virtualenvwrapper][virtualenvwrapper]

顾名思义，它是virtualenv的扩展，提供了更加易用的命令。

* 安装

		$ pip install virtualenvwrapper

* 创建：

        $ mkvirtualenv env1
        Installing
        distribute..........................................
        ....................................................
        ....................................................
        ...............................done.
        virtualenvwrapper.user_scripts Creating /Users/dhellmann/Envs/env1/bin/predeactivate
        virtualenvwrapper.user_scripts Creating /Users/dhellmann/Envs/env1/bin/postdeactivate
        virtualenvwrapper.user_scripts Creating /Users/dhellmann/Envs/env1/bin/preactivate
        virtualenvwrapper.user_scripts Creating /Users/dhellmann/Envs/env1/bin/postactivate  New python executable in env1/bin/python


* 切换

        (env2)$ workon env1
        (env1)$

[virtualenvwrapper]: http://virtualenvwrapper.readthedocs.org/en/latest/