Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:13:57) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> thistuple = ('apple', 'banana', 'cherry')
>>> if 'apple' in thistuple:
	print('Yes, "apple" is in the fruits tuple')

	
Yes, "apple" is in the fruits tuple
>>> thistuple = ('Python',)*3
>>> print(thistuple)
('Python', 'Python', 'Python')
>>> thistuple = ('Python')*3
>>> print(thistuple)
PythonPythonPython
>>> thistuple1 = (1, 2, 3, 4)
>>> thistuple2 = (5, 6)
>>> thistuple = thistuple1 + thistuple2
>>> print(thistuple)
(1, 2, 3, 4, 5, 6)
>>> x = (3, 4, 5, 6)
>>> x + x + (1, 2, 3)
(3, 4, 5, 6, 3, 4, 5, 6, 1, 2, 3)
>>> thistuple = ('apple', 'banana', 'cherry')
>>> print(len(thistuple))
3
>>> thistuple = tuple(('apple', 'banana', 'cherry'))
>>> print(thistuple)
('apple', 'banana', 'cherry')
>>> thislist = [3, 4, 5, 6, "A", "B"]
>>> thistuple = tuple(thislist)
>>> print(thistuple)
(3, 4, 5, 6, 'A', 'B')
>>> 
