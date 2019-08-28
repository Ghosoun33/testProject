Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:13:57) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> age = 36
>>> txt = 'My name is John, I am ' + age
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    txt = 'My name is John, I am ' + age
TypeError: can only concatenate str (not "int") to str
>>> age = 36
>>> txt = 'My name is John, and I am {}'
>>> print(txt.format(age))
My name is John, and I am 36
>>> quantity = 3
>>> itemno = 567
>>> price = 49.95
>>> myorder = 'I want {} pieces of item {} for {} dollars.'
>>> print(myorder.format(quantity, itemno, price))
I want 3 pieces of item 567 for 49.95 dollars.
>>> quantity = 3
>>> itemno = 567
>>> price = 49.95
>>> myorder = 'I want to pay {2} dollars for {0} pieces of item {1}.'
>>> print(myorder.format(quantity, itemno, price))
I want to pay 49.95 dollars for 3 pieces of item 567.
>>> 
