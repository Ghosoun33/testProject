Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> quantity = 3
>>> itemno = 567
>>> price = 49
>>> myorder = 'I want {0} pieces of item number {1} for {2:.2f} dollars.'
>>> print(myorder.format(quantity, itemno, price))
I want 3 pieces of item number 567 for 49.00 dollars.
>>> age = 36
>>> name ='John'
>>> txt = 'His name is {1}. {1} is {0} years old.'
>>> print(txt.format(age, name))
His name is John. John is 36 years old.
>>> myorder = 'I have a {carname}, it is a {model}.'
>>> print(myorder.format(carname = 'Ford', model = 'Mustang'))
I have a Ford, it is a Mustang.
>>> 
