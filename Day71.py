Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import mysql.connector
>>> mydb = mysql.connector.connect(
	host='localhost',
	user='myusername',
	passwd='mypassword',
	database='mydatabase'
	)
>>> mycursor = my.cursor()
>>> sql = 'INSERT INTO customers (name, address)VALUES(%s, %s)'
>>> val = ('John', 'Highway 21')
>>> mycursor.execute(sq1, val)
>>> mydb.commit()
>>> print(mycursor.rowcount, 'record inserted.')

>>> mycursor = mydb.cursor()
>>> sql = 'INSERT INTO customers (name, address)VALUES(%s, %s)'
>>> val = ('Michelle', 'Blue Village')
>>> mycursor.execute(sq1, val)
>>> mydb.commit()
>>> print('1 record inserted, ID:', mycursor.lastrowid)

>>> mycursor = mydb.cursor()
>>> mycursor.execute('SELECT * FROM customers')
>>> myresult = mycursor.fetchall()
>>> for x in meresult:
	print(x)

>>> mycursor = mydb.cursor()
>>> sql = 'SELECT * FROM customers WHERE address Like "%way%"'
>>> mycursor.execute(sq1)
>>> myresult = mycursor.fetchall()
>>> for x in meresult:
	print(x)

>>>
