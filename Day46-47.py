Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Library():
	def __init__(self, book = 300, shelf = 45):
		self.book = book
		self.shelf = shelf

		
>>> myLib = Library(shelf = 45, book = 300)
>>> class science_section(Library):
	def __init__(self, name, book = 300, shelf = 45):
		super().__init__(book, shelf)
		self.name = name
	def printContent(self):
		print('Section name:', self.name)
		print('Number of shelves:', self.shelf)
		print('Number of books:', self.book)

		
>>> mysection = science_section(name = 'physics Books')
>>> mysection.printContent()
Section name: physics Books
Number of shelves: 45
Number of books: 300
>>> mysection.book = 20
>>> mysection.shelf = 4
>>> print('\nafter chaging the content\n')

after chaging the content

>>> mysection.printContent()
Section name: physics Books
Number of shelves: 4
Number of books: 20
>>> 
