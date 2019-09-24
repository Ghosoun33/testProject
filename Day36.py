Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:13:57) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def myfunc(n):
	return lambda a : a * n

>>> mydoubler = myfunc(2)
>>> print(mydoubler(11))
22
>>> mydoubler = myfunc(3)
>>> print(mydoubler(11))
33
>>> mydoubler = myfunc(2)
>>> print(mydoubler(11))
22
>>> mydoubler = myfunc(3)
>>> print(mydoubler(11))
33
>>> 
