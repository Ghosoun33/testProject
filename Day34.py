Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:13:57) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def my_function(food):
	for x in food:
		print(x)

		
>>> fruits = ['apple', 'banana', 'cherry']
>>> my_function(fruits)
apple
banana
cherry
>>> def my_function(x):
	return 5 * x

>>> print(my_function(3))
15
>>> print(my_function(5))
25
>>> print(my_function(9))
45
>>> def my_function(child3, child2, child1):
	print('The youngest child is ' + child3)

	
>>> my_function(child1 = 'Emil', child2 = 'Tobias', child3 = 'Linus')
The youngest child is Linus
>>> def my_function(*kids):
	print('The youngest child is ' + kids[2])

	
>>> my_function('Emil', 'Tobias', 'Linus')
The youngest child is Linus
>>> def tri_recursion(k):
	if(k>0):
		result = k+tri_recursion(k-1)
		print(result)
	else:
		result = 0
		return result
	print('\n\nRecursion Example Results')
	tri_recursion(6)

	
>>> 
