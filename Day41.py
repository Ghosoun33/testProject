Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:13:57) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Myclass:
	x = 5

	
>>> print(Myclass)
<class '__main__.Myclass'>
>>> p1 = Myclass()
>>> print(p1.x)
5
>>> class person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

		
>>> p1 = person("John", 36)
>>> print(p1.name)
John
>>> print(p1.age)
36
>>> class person:
	def __init__(mysillyobject, name, age):
		mysillyobject.name = name
		mysillyobject.age = age
	def myfunc(abc):
		print('Hello my name is '+ abc.name)

		
>>> p1 = person('John', 36)
>>> p1.myfunc()
Hello my name is John
>>> 
