Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import re
>>> str = 'The rain in spain'
>>> x = re.findall('ai', str)
>>> print(x)
['ai', 'ai']
>>> x = re.findall('portugal', str)
>>> print(x)
[]
>>> if (x):
	print('Yes, there is at least match!')
else:
	print('No match')

	
No match
>>> x = re.search('\s', str)
>>> print('The first white-space character in position:', x.start())
The first white-space character in position: 3
>>> x = re.search('portugal', str)
>>> print(x)
None
>>> x = re.split('\s', str)
>>> print(x)
['The', 'rain', 'in', 'spain']
>>> 
