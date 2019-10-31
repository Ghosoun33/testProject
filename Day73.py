Python 3.7.4


>>> import mysql.connector
>>> mydb = mysql.connector.connect(
	host='localhost',
	user='myusername',
	passwd='mypassword',
	database='mydatabase'
	)
>>> mycursor = mydb.cursor()
>>> sql = "update customers set address = 'Canyon 123' where address = 'Valley 345'"
>>> mycursor.execute(sql)
>>> mydb.commit()
>>> print(mycursor.rowcount, "records affected")

>>> mycursor = mydb.cursor()
>>> sql = ("SELECT * FROM customers limit 5")
>>> myresult = mycursor.fetchall()
>>> for x in myresult:
    print(x)

>>> mycursor = mydb.cursor()
>>> sql = ("SELECT * FROM customers limit 5 offset 2")
>>> myresult = mycursor.fetchall()
>>> for x in myresult:
    print(x)

>>>
