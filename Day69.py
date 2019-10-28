Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> f = open('demofile.txt')

>>> f = open('demofile.txt', 'rt')

>>> f = open('demofile.txt', 'r')
>>> print(f.read())

>>> f = open('demofile.txt', 'r')
>>> print(f.read(5))

>>> f = open('demofile.txt', 'r')
>>> print(f.readline())

>>> f = open('demofile.txt', 'r')

>>> print(f.readline())
>>> f = open('demofile.txt', 'r')
>>> for x in f:
	print(x)

>>> f = open('demofile.txt', 'r')
>>> print(f.readline())
>>> f.close()
