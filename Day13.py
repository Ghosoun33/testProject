Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:13:57) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> text =  'Please, I want {} sandwishes and {} donutes'
>>> print('Before:\n', text)
Before:
 Please, I want {} sandwishes and {} donutes
>>> text = text.replace('I', 'We')
>>> text = text.format(5, 7)
>>> text = text.upper()
>>> print(text)
PLEASE, WE WANT 5 SANDWISHES AND 7 DONUTES
>>> 
