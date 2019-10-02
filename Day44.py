Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:13:57) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class person:
	def __init__(self, fname, lname):
		self.firstname = fname
		self.lastname = lname
	def printname(self):
		print(self.firstname, self.lastname)

		
>>> class Student(person):
	def __init__(self, fname, lname):
		super().__init__(fname, lname)

		
>>> x = Student('Mike', 'Olsen')
>>> x.printname()
Mike Olsen
>>> class Student(person):
	def __init__(self, fname, lname):
		super().__init__(fname, lname)
		self.graduationyear = 2019

		
>>> x = Student('Mike', 'Olsen')
>>> print(x.graduationyear)
2019
>>> class Student(person):
	def __init__(self, fname, lname, year):
		super().__init__(fname, lname)
		self.graduationyear = year

		
>>> x = Student('Mike', 'Olsen', 2019)
>>> print(x.graduationyear)
2019
>>> class Student(person):
	def __init__(self, fname, lname, year):
		super().__init__(fname, lname)
		self.graduationyear = year
	def welcome(self):
		print("welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

		
>>> x = Student('Mike', 'Olsen', 2019)
>>> x.welcome()
welcome Mike Olsen to the class of 2019
>>> 
