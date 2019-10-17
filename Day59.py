Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import re
>>> str = 'The rain in spain'
>>> x = re.sub('\s', '9', str)
>>> print(x)
The9rain9in9spain
>>> x = re.sub('\s', '9', str, 2)
>>> print(x)
The9rain9in spain
>>> x = re.search('ai', str)
>>> print(x)
<re.Match object; span=(5, 7), match='ai'>
>>> x = re.search(r'\bs\w+', str)
>>> print(x.span())
(12, 17)
>>> x = re.search(r'\bs\w+', str)
>>> print(x.string)
The rain in spain
>>> x = re.search(r'\bs\w+', str)
>>> print(x.group())
spain
>>> 
