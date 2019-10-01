Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:13:57) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class person:
	def __init__(self, fname, lname):
		self.firstname = fname
		self.lastname = lname
	def printname(self):
		print(self.firstname, self.lastname)

		
>>> x = person('John', 'Doe')
>>> x.printname()
John Doe
>>> class person:
	def __init__(self, fname, lname):
		self.firstname = fname
		self.lastname = lname
	def printname(self):
		print(self.firstname, self.lastname)

		
>>> class Student(person):
	pass

>>> x = Student('Mile', 'Olsen')
>>> x.printname()
Mile Olsen
>>> class person:
	def __init__(self, fname, lname):
		self.firstname = fname
		self.lastname = lname
	def printname(self):
		print(self.firstname, self.lastname)

		
>>> class Student(person):
	def __init__(self, fname, lname):
		person.__init__(self, fname, lname)

		
>>> x = Student('Mile', 'Olsen')
>>> x.printname()
Mile Olsen
>>> 
