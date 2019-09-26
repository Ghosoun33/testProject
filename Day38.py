Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:13:57) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> cars = ['Ford', 'Volvo', 'BMW']
>>> for x in cars:
	print(x)

	
Ford
Volvo
BMW
>>> cars.append('Honda')
>>> print(cars)
['Ford', 'Volvo', 'BMW', 'Honda']
>>> cars.pop(1)
'Volvo'
>>> cars.remove('Ford')
>>> print(cars)
['BMW', 'Honda']
>>> 
