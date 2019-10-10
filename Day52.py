Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import datetime
>>> x = datetime.datetime.now()
>>> print(x)
2019-10-10 11:24:05.032798
>>> import datetime
>>> x = datetime.datetime.now()
>>> print(x.year)
2019
>>> print(x.strftime('%A'))
Thursday
>>> import datetime
>>> x = datetime.datetime(2020, 5, 17)
>>> print(x)
2020-05-17 00:00:00
>>> import datetime
>>> x = datetime.datetime(2018, 6, 1)
>>> print(x.strftime('%B'))
June
>>> 
