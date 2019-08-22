Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:13:57) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = 5
>>> y = 'John'
>>> print(x)
5
>>> print(y)
John
>>> x = 4 # x is of type int
>>> x = 'sally' # x is now of type str
>>> print(x)
sally
>>> x = 'John'
>>> # is the same as
>>> x = 'John'
>>> print(x)
John
>>> x, y, z = 'Orange', 'Banana', 'Cherry'
>>> print(x)
Orange
>>> print(y)
Banana
>>> print(z)
Cherry
>>> x = y = z = 'Orange'
>>> print(x)
Orange
>>> print(y)
Orange
>>> print(z)
Orange
>>> x = 'awesome'
>>> print('python is' + x)
python isawesome
>>> x = 'python is '
>>> y = 'awesome'
>>> z = x + y
>>> print(z)
python is awesome
>>> x = 5
>>> y = 10
>>> print(x + y)
15
>>> x = 5
>>> y = 'John'
>>> print(x + y)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    print(x + y)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> 
