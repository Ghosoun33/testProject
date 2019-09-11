Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:13:57) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> thisdict = {
	'brand': 'Ford',
	'model': 'Mustang',
	'year': 1964
	}
>>> if 'model' in thisdict:
	print("Yes, 'model' is one of the keys in the thisdict dictonary")

	
Yes, 'model' is one of the keys in the thisdict dictonary
>>> print(len(thisdict))
3
>>> thisdict['color'] = 'red'
>>> print(thisdict)
{'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}
>>> {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}
{'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}
>>> thisdict.pop('model')
'Mustang'
>>> print(thisdict)
{'brand': 'Ford', 'year': 1964, 'color': 'red'}
>>> thisdict.popitem()
('color', 'red')
>>> print(thisdict)
{'brand': 'Ford', 'year': 1964}
>>> thisdict = {
	'brand': 'Ford',
	'model': 'Mustang',
	'year': 1964
	}
>>> del thisdict['model']
>>> print(thisdict)
{'brand': 'Ford', 'year': 1964}
>>> del thisdict
>>> print(thisdict)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    print(thisdict)
NameError: name 'thisdict' is not defined
>>> thisdict = {
	'brand': 'Ford',
	'model': 'Mustang',
	'year': 1964
	}
>>> thisdict.clear()
>>> print(thisdict)
{}
>>> 
