Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:13:57) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> animal = {
	'name': 'pigeon',
	'type': 'bird',
	'skincover': 'feathers'
	}
>>> x = animal.get('type')
>>> print(x)
bird
>>> animal['skincover'] = 'nothing'
>>> print(animal)
{'name': 'pigeon', 'type': 'bird', 'skincover': 'nothing'}
>>> 
