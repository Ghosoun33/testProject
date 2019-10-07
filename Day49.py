Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = 300
>>> def myfunc():
	x = 200
	print(x)

	
>>> myfunc()
200
>>> print(x)
300
>>> def myfunc():
	global x
	x = 300

	
>>> myfunc()
>>> print(x)
300
>>> x = 300
>>> def myfunc():
	global x
	x = 200

	
>>> myfunc()
>>> print(x)
200
>>> 
