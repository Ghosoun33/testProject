Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:13:57) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def my_function():
	print('Hello from a function')

	
>>> my_function()
Hello from a function
>>> def my_function(fname):
	print(fname + ' Refsnes')

	
>>> my_function('Emil')
Emil Refsnes
>>> my_function('Tobias')
Tobias Refsnes
>>> my_function('Linus')
Linus Refsnes
>>> def my_function(country = 'Norway'):
	print('I am from ' + country)

	
>>> my_function('Sweden')
I am from Sweden
>>> my_function('India')
I am from India
>>> my_function()
I am from Norway
>>> my_function('Brazil')
I am from Brazil
>>> 
