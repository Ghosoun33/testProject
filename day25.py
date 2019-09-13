Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:13:57) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> set = {1, 3, 5, 7, 8}
>>> set.update([4, 8, 12])
>>> print(set)
{1, 3, 4, 5, 7, 8, 12}
>>> set.remove(8)
>>> print(set)
{1, 3, 4, 5, 7, 12}
>>> set.clear()
>>> print(set)
set()
>>> 
