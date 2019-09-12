Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:13:57) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> thisdict = {
	'brand': 'Ford',
	'model': 'Mustang',
	'year': 1964
	}
>>> mydict = thisdict.copy()
>>> print(mydict)
{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
>>> mydict = dict(thisdict)
>>> print(mydict)
{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
>>> myfamily = {
	'child1' : {
		'name' : 'Emil',
		'year' : 2004
		},
	'child2' : {
		'name' : 'Tobias',
		'year' : 2007
		},
	'child3' : {
		'name' : 'Linus',
		'year' : 2011
		}
	}
>>> print(myfamily)
{'child1': {'name': 'Emil', 'year': 2004}, 'child2': {'name': 'Tobias', 'year': 2007}, 'child3': {'name': 'Linus', 'year': 2011}}
>>> child1 = {
	'name' : 'Emil',
	'year' : 2004
	}
>>> child2 = {
	'name' : 'Tobias',
        'year' : 2007
	}
>>> child3 = {
	'name' : 'Linus',
	'year' : 2011
	}
>>> myfamily = {
	'child1' : child1,
	'child2' : child2,
	'child3' : child3
	}
>>> print(myfamily)
{'child1': {'name': 'Emil', 'year': 2004}, 'child2': {'name': 'Tobias', 'year': 2007}, 'child3': {'name': 'Linus', 'year': 2011}}
>>> thisdict = dict(brand='ford', model='mustang', year=1964)
>>> print(thisdict)
{'brand': 'ford', 'model': 'mustang', 'year': 1964}
>>> 
