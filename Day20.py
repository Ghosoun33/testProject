Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:13:57) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> thisset = {}
>>> print(thisset)
{}
>>> thisset = {'apple', 'banana', 'cherry'}
>>> print(thisset)
{'cherry', 'apple', 'banana'}
>>> thisset = {'Ahmad', 'Ahmad', 1, 2, 1, 5}
>>> print(thisset)
{1, 2, 5, 'Ahmad'}
>>> thisset = {'apple', 'banana', 'cherry'}
>>> for x in thisset:
	print(x)

	
cherry
apple
banana
>>> print('banana' in thisset)
True
>>> thisset.add('orange')
>>> print(thisset)
{'cherry', 'apple', 'orange', 'banana'}
>>> thisset.update(['orange', 'mango', 'grapes'])
>>> print(thisset)
{'mango', 'apple', 'grapes', 'orange', 'banana', 'cherry'}
>>> 
