Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:13:57) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class person:
	def __init__(self, name, age):
		self.name = name
		self.age = age
	def myfunc(self):
		print('Hello my name is ' + self.name)

		
>>> p1 = person('John', 36)
>>> p1.myfunc()
Hello my name is John
>>> p1 = person('John', 36)
>>> p1.age = 40
>>> print(p1.age)
40
>>> del p1.age
>>> print(p1.age)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    print(p1.age)
AttributeError: 'person' object has no attribute 'age'
>>> del p1
>>> print(p1)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    print(p1)
NameError: name 'p1' is not defined
>>> 
