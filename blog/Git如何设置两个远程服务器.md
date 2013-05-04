## Git如何设置两个远程服务器
Category: git  
Tags: git, remote, fetch   
Date: 2013-05-04


>最近把这段时间写的代码push到heroku时出现了问题，运行`git push`后一直没有响应，后来发现`git pull --rebase`也是没有响应，一直没找到原因。因为不想代码总在本地放着，所以想把代码存放在github和heroku两个地方，平时向github提交，开发到一定阶段再push到heroku。

<br>

下面将一步步的进行操作：


* 建立一个空的git repositoy作为我们的working directory：

		➜  git-demo  git init local
		Initialized empty Git repository in ~/workspace/git-demo/local/.git/
		➜  git-demo  cd local
	
	
* 添加文件readme.md,并提交到本地：

		➜  local git:(master) touch readme.md
		➜  local git:(master) git add .      
		➜  local git:(master) git commit -m "killera: Add readme file"


* 在本地文件系统中创建一个git repository作为remote repository，叫做github：

		➜  git-demo  ls
		local
		➜  git-demo  git init github --bare
		Initialized empty Git repository in ~/workspace/git-demo/github/

* 类似的，在本地文件系统创建另一个remote repository， 叫做heroku：

		➜  git-demo  git init heroku --bare
		Initialized empty Git repository in ~/workspace/git-demo/heroku/
		➜  git-demo  ls 
		github heroku local
		➜  git-demo  
		
* 将local中的代码提交到github仓库：

		➜  local git:(master) git remote add origin ~/workspace/git-demo/github
		➜  local git:(master) git push origin master
		Counting objects: 3, done.
		Writing objects: 100% (3/3), 230 bytes, done.
		Total 3 (delta 0), reused 0 (delta 0)
		Unpacking objects: 100% (3/3), done.
		To ~/workspace/git-demo/github
		* [new branch]      master -> master
		
* 此时我们看local/.git/config文件，多了一项配置：

		[remote "origin"]
		url = ~/workspace/git-demo/github
		fetch = +refs/heads/*:refs/remotes/origin/*
	这是我们执行`git remote add`的结果。
	
* 同样，如果我们想把代码提交到heroku，那么需要再添加一个remote ’heroku‘并提交代码到这个remote就行了：

		➜  local git:(master) git remote add heroku ~/workspace/git-demo/heroku
		➜  local git:(master) git push heroku master
		Counting objects: 3, done.
		Writing objects: 100% (3/3), 230 bytes, done.
		Total 3 (delta 0), reused 0 (delta 0)
		Unpacking objects: 100% (3/3), done.
		To ~/workspace/git-demo/heroku
		 * [new branch]      master -> master
		➜  local git:(master) 
		
	再查看config文件，多了一项：
	
		[remote "heroku"]
		url = ~/workspace/git-demo/heroku
		fetch = +refs/heads/*:refs/remotes/heroku/*
	
	通过git命令查看所有remote：
	
		➜  local git:(master) git remote -v
		heroku	~/workspace/git-demo/heroku (fetch)
		heroku	~/workspace/git-demo/heroku (push)
		origin	~/workspace/git-demo/github (fetch)
		origin	~/workspace/git-demo/github (push)

* 如果我们想在一次push时把代码提交到github的同时也提交到heroku，那么可以添加一个push的url到origin：
	
		➜  local git:(master) git remote set-url --add --push origin ~/workspace/git-demo/github
		➜  local git:(master) git remote set-url --add --push origin ~/workspace/git-demo/heroku
		
	这样在git push的时候会把代码提交到两个remote repositories。
	
	查看config文件:
	
		[remote "origin"]
        	url = ~/workspace/git-demo/github
        	fetch = +refs/heads/*:refs/remotes/origin/*        	
			pushurl = ~/workspace/git-demo/heroku
			pushurl = ~/workspace/git-demde></pre>
			
* 另外一种方式为:
	
		➜  local git:(master) git remote set-url --add origin ~/workspace/git-demo/heroku
		
	这样在config文件中不是添加pushurl而是添加url，在push时同样会提交到两个repositories。
	
	不同的是当pull时，它会从第一个设置的url去更新代码。也就是说，如果我们改动config文件中的[remote "origin"]，把heroku的url放在github之前，在执行`git pull origin master`时会从heroku更新代码。

* 这样往往会造成困扰，所以我们可以添加一个单独的remote配置：
	
		[remote "both"]
			url = ~/workspace/git-demo/github
			url = ~/workspace/git-demo/heroku
	然后执行`git push both`，就会将代码push到两个repositories了。