Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:13:57) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> thislist = ['apple', 'banana', 'cherry']
>>> print(len(thislist))
3
>>> thislist = ['apple', 'banana', 'cherry']
>>> thislist.append('orange')
>>> print(thislist)
['apple', 'banana', 'cherry', 'orange']
>>> thislist = ['apple', 'banana', 'cherry']
>>> thislist.insert(1, 'orange')
>>> print(thislist)
['apple', 'orange', 'banana', 'cherry']
>>> thislist = ['apple', 'banana', 'cherry']
>>> thislist.remove('banana')
>>> print(thislist)
['apple', 'cherry']
>>> thislist = ['apple', 'orange', 'banana', 'cherry', 'orange']
>>> thislist.remove('orange')
>>> print(thislist)
['apple', 'banana', 'cherry', 'orange']
>>> thislist = ['apple', 'banana', 'cherry']
>>> thislist.pop()
'cherry'
>>> print(thislist)
['apple', 'banana']
>>> thislist.pop(1)
'banana'
>>> print(thislist)
['apple']
>>> thislist = ['apple', 'banana', 'cherry']
>>> thislist.clear()
>>> print(thislist)
[]
>>> thislist = ['apple', 'banana', 'cherry']
>>> mylist = thislist.copy()
>>> print(mylist)
['apple', 'banana', 'cherry']
>>> thislist = ['apple', 'banana', 'cherry']
>>> mylist = list(thislist)
>>> print(mylist)
['apple', 'banana', 'cherry']
>>> thislist = list(('apple', 'banana', 'cherry'))
>>> print(thislist)
['apple', 'banana', 'cherry']
>>> 
