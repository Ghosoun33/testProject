Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> mytuple = ('apple', 'banana', 'cherry')
>>> myit = iter(mytuple)
>>> print(next(myit))
apple
>>> print(next(myit))
banana
>>> print(next(myit))
cherry
>>> mystr = 'banana'
>>> myit = iter(mystr)
>>> print(next(myit))
b
>>> print(next(myit))
a
>>> print(next(myit))
n
>>> print(next(myit))
a
>>> print(next(myit))
n
>>> print(next(myit))
a
>>> mytuple = ('apple', 'banana', 'cherry')
>>> for x in mytuple:
	print(x)

	
apple
banana
cherry
>>> myste = 'banana'
>>> for x in mystr:
	print(x)

	
b
a
n
a
n
a
>>> class MyNumbers:
	def __iter__(self):
		self.a = 1
		return self
	def __next__(self):
		x = self.a
		self.a += 1
		return x

	
>>> myclass = MyNumbers()
>>> myiter = iter(myclass)
>>> print(next(myiter))
1
>>> print(next(myiter))
2
>>> print(next(myiter))
3
>>> print(next(myiter))
4
>>> print(next(myiter))
5
>>> class MyNumbers:
	def __iter__(self):
		self.a = 1
		return self
	def __next__(self):
		if self.a <= 20:
			x = self.a
			self.a += 1
			return x
		else:
			raise StopIteration

		
>>> myclass = MyNumbers()
>>> myiter = iter(myclass)
>>> for x in myiter:
	print(x)

	
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
>>> 
