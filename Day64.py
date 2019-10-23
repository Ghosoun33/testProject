Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> try:
	print(x)
except:
	print('An exception occurred')

	
An exception occurred
>>> print(x)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    print(x)
NameError: name 'x' is not defined
>>> try:
	print(x)
except NameError:
	print('Variable x is not defined')
except:
	print('Something else went wrong')

	
Variable x is not defined
>>> try:
	print('Hello')
except:
	print('Something went wrong')
else:
	print('Nothing went wrong')

	
Hello
Nothing went wrong
>>> try:
	print(x)
except:
	print('Something went wrong')
finally:
	print('The "try execpt" is finished')

	
Something went wrong
The "try execpt" is finished
>>> 
