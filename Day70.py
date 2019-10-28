Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import mysql.connector
>>> mydb = mysql.connector.connector(
	host='localhost',
	user='myusername',
	passwd='mypassword'
	)
>>> print(mydb)

>>> mycursor.execute('SHOW DATABASES')
>>> for x in mycursor:
	print(x)

>>>
