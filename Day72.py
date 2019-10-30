Python 3.7.4

>>> import mysql.connector
>>> mydb = mysql.connector.connect(
	host='localhost',
	user='myusername',
	passwd='mypassword',
	database='mydatabase'
	)
>>> mycursor = mydb.cursor()
>>> sql = 'SELECT * FROM customers ORDER BY name'
>>> mycursor.execute(sq1)
>>> myresult = mycursor.fetchall()
>>> for x in meresult:
	print(x)


>>> mycursor = mydb.cursor()
>>> sql = 'SELECT * FROM customers ORDER BY name DESC'
>>> mycursor.execute(sq1)
>>> myresult = mycursor.fetchall()
>>> for x in meresult:
	print(x)


>>> mycursor = mydb.cursor()
>>> sql = "DELETE FROM customers WHERE address = 'Mountain 21'"
>>> mycursor.execute(sq1)
>>> mydb.commit()
>>> print(mycursor.rowcount, 'record(s) deleted')

>>> mycursor = mydb.cursor()
>>> sql = 'DROP TABLE customers'
>>> mycursor.execute(sq1)

>>> mycursor = mydb.cursor()
>>> sql = 'DROP TABLE IF EXISTS customers'
>>> mycursor.execute(sq1)
>>>
