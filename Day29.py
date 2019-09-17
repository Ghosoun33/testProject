Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:13:57) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> fruits = ['apple', 'banana', 'cherry']
>>> for x in fruits:
	print(x)

	
apple
banana
cherry
>>> for x in 'banana':
	print(x)

	
b
a
n
a
n
a
>>> for x in fruits:
	print(x)
	if x == 'banana':
		break

	
apple
banana
>>> for x in fruits:
	if x == 'banana':
		break
	print(x)

	
apple
>>> for x in fruits:
	if x == 'banana':
		continue
	print(x)

	
apple
cherry
>>> 
