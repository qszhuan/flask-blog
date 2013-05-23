##Cookies in Python
Category: python  
Tags: cookie, requests, set_cookie, python
Date: 2013-05-09


If you want to use cookies in web development, [requests][requests] library is a very wise choice.


If a response contains some Cookies, you can get quick access to them:

	>>> url = 'http://www.google.com'
	>>> r = requests.get(url)
	>>> r.cookies
	
If you want to send your own cookies to server, you can simple add `cookies` parameters:
	
	>>>cookies = dict('name'='value')
	>>> r = requests.get(url, cookies=cookies)

If you want to set the `domain` or `path` value in cookies, just add them into the `cookies` dict which you created before.

Also, you can use `create_cookie` method that requests supplies, you can import it by `from requests.cookies import create_cookie`, it will exactly do the same job.

	c = create_cookie('aaa', 'bbb', domain='localhost')

The cookies created are instances of `cookielib.Cookie`, they are held by `requests.cookies.RequestsCookieJar`.

**requests** is a very useful library, and what's more, it is simple. Go to [requests][requests] to see more.


[requests]: http://docs.python-requests.org/en/latest/