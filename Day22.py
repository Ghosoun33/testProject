Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:13:57) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> thisdict = {}
>>> print(thisdict)
{}
>>> thisdict = {
	'brand': 'Ford',
	'model': 'Mustang',
	'year': 1964
	}
>>> print(thisdict)
{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
>>> x = thisdict['model']
>>> print(x)
Mustang
>>> x = thisdict.get('model')
>>> print(x)
Mustang
>>> thisdict['year'] = 2018
>>> print(thisdict)
{'brand': 'Ford', 'model': 'Mustang', 'year': 2018}
>>> for x in thisdict:
	print(x)

	
brand
model
year
>>> for x in thisdict:
	print(thisdict[x])

	
Ford
Mustang
2018
>>> for x in thisdict.values():
	print(x)

	
Ford
Mustang
2018
>>> print(thisdict.values())
dict_values(['Ford', 'Mustang', 2018])
>>> for x, y in thisdict.items():
	print(x, y)

	
brand Ford
model Mustang
year 2018
>>> print(thisdict.items())
dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 2018)])
>>> 
