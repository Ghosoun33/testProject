Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> price = 49
>>> txt = 'The price is {} dollars'
>>> print(txt.format(price))
The price is 49 dollars
>>> txt = 'The price is {:.2f} dollars'
>>> print(txt.format(price))
The price is 49.00 dollars
>>> quantity = 3
>>> itemno = 567
>>> price = 49
>>> myorder = 'I want {} pieces of item number {} for {:.2f} dollars.'
>>> print(myorder.format(quantity, itemno, price))
I want 3 pieces of item number 567 for 49.00 dollars.
>>> 
