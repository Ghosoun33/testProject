Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:13:57) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def power(x,y):
	if(y==1):
		return x
	else:
		return x*power(x,y-1)
	print(power(5,3))

	
>>> List = [-4, -6, -5, -1, 2, 3, 7, 9, 88]
>>> def positive(lst):
	List1 = list(filter(lambda n: (n >= 0), lst))
	return List1

>>> print(positive(List))
[2, 3, 7, 9, 88]
>>> 
