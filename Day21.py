Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:13:57) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> thisset = {'apple', 'banana', 'cherry'}
>>> print(len(thisset))
3
>>> thisset.remove('banana')
>>> print(thisset)
{'cherry', 'apple'}
>>> thisset.discard('banana')
>>> print(thisset)
{'cherry', 'apple'}
>>> x = thisset.pop()
>>> print(x)
cherry
>>> print(thisset)
{'apple'}
>>> thisset.clear()
>>> print(thisset)
set()
>>> del thisset
>>> print(thisset)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    print(thisset)
NameError: name 'thisset' is not defined
>>> thisset = set(('apple', 'banana', 'cherry'))
>>> print(thisset)
{'cherry', 'banana', 'apple'}
>>> 
