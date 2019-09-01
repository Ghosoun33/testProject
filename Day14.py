Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:13:57) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s = []
>>> print(s)
[]
>>> numbers = [1, 2, 3, 4, 5]
>>> print(numbers)
[1, 2, 3, 4, 5]
>>> thislist = ['apple', 'banana', 'cherry']
>>> print(thislist)
['apple', 'banana', 'cherry']
>>> thislist = ['apple', 'banana', 'cherry', 1, 2, 3]
>>> print(thislist)
['apple', 'banana', 'cherry', 1, 2, 3]
>>> numbers = [1.5, 2.5, 3.5, 4.5]
>>> print(numbers)
[1.5, 2.5, 3.5, 4.5]
>>> thislist = ['apple', 'banana', 'cherry']
>>> print(thislist[1])
banana
>>> thislist = ['apple', 'banana', 'cherry']
>>> for x in thislist:
	print(x)

	
apple
banana
cherry
>>> numbers = [1, 2, 3, 4, 5]
>>> for x in numbers:
	print(x)

	
1
2
3
4
5
>>> thislist = ['apple', 'banana', 'cherry']
>>> thislist[1] = 'blackcurrant'
>>> print(thislist)
['apple', 'blackcurrant', 'cherry']
>>> thislist = ['apple', 'banana', 'cherry']
>>> del thislist[0]
>>> print(thislist)
['banana', 'cherry']
>>> thislist = ['apple', 'banana', 'cherry']
>>> del thislist
>>> print(thislist)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    print(thislist)
NameError: name 'thislist' is not defined
>>> 
