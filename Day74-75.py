Python 3.7.4

>>> txt = open("hello.txt", "rt")
>>> print(txt.readline())
>>> txt = open("hello.txt", "a")
>>> txt.write("The best way we learn anything is by practice and exercise questions")
>>> txt = open("hello.txt", "rt")
>>> print(txt.readline())
>>>
>>>
>>> mydb = mysql.connector.connect(

    host="localhost",
    user="myusername",
    passwd="mypassword",
    db="mydatabase"
)
>>> mycursor = mydb.cursor()
>>> mycursor.execute("CREATE DATABASE mydatabase")
>>> mycursor.execute("CREATE TABLE mydatabase (id INT AUTO_INCREMENT PRIMARY KEY, fname VARCHAR(255), lname VARCHAR(255),"
                 " Age INT(25), Gender VARCHAR(255), salary INT(25))")
>>> sql = "INSERT INTO mydatabase (fname, lname, Age, Gender, salary) " \
      "VALUES (%s, %s, %s, %s, %s )"
>>> val = [
  ('Ahmad', 'Ali', 30, 'Male', 10000),
  ('Khalid', 'Muhammad', 34, 'Male', 7000),
  ('Norah', 'Saleh', 29, 'Female', 7000)
]
>>> mycursor.executemany(sql, val)
>>> mydb.commit()
>>> print(mycursor.rowcount, "was inserted.")

>>> mycursor.execute("SELECT * FROM mydatabase")
>>> myresult = mycursor.fetchall()
>>> for x in myresult:
  print(x)

>>> myresult = mycursor.fetchall()
>>> for x in myresult:
  print(x)

>>> mycursor.execute("delete FROM mydatabase where Age = 34")
>>> mycursor.execute("SELECT * FROM mydatabase")
>>> myresult = mycursor.fetchall()
>>> for x in myresult:
  print(x)
