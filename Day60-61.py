Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import json
>>> week = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
>>> x = json.dumps(week)
>>> print(x)
["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
>>> 
>>> 
>>> import re
>>> txt = "data is the new oil"
>>> x = re.findall("data", txt)
>>> print(x)
['data']
>>> 
