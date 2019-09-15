Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:13:57) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = 33
>>> b = 200
>>> if b > a:
	print('b is greater than a')

	
b is greater than a
>>> if b > a:
print('b is greater than a')
SyntaxError: expected an indented block
>>> a = 33
>>> b = 33
>>> if b > a:
	print('b is greater than a')
elif a == b:
	print('a and b are equal')

	
a and b are equal
>>> a = 200
>>> b = 33
>>> if b > a:
	print('b is greater than a')
elif a == b:
	print('a and b are equal')
else:
	print('a is greater than b')

	
a is greater than b
>>> a = 200
>>> b = 33
>>> if b > a:
	print('b is greater than a')
else:
	print('b is not greater than a')

	
b is not greater than a
>>> a = 200
>>> b = 33
>>> if a > b: print('a is greater than b')

a is greater than b
>>> a = 2
>>> b = 330
>>> print('A') if a > b else print('B')
B
>>> a = 330
>>> b = 330
>>> print('A') if a > b else print()

>>> 
>>> print('A') if a > b else print('=') if a == b else print('B')
=
>>> 
>>> a = 200
>>> b = 33
>>> c = 500
>>> if a > b and c > a:
	print('Both conditions are True')

	
Both conditions are True
>>> if a > b or a > c:
	print('At least one of the conditions is True')

	
At least one of the conditions is True
>>> x = 41
>>> if x > 10:
	print('Above ten,')
	if x > 20:
		print('and also above 20!,')
	else:
		print('but not above 20.')

		
Above ten,
and also above 20!,
>>> 
