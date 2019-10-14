Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import json
>>> x = '{"name":"John", "age":30, "city":"New York"}'
>>> y = json.loads(x)
>>> print(y["age"])
30
>>> import json
>>> x = {
	"name":"John",
	"age":30,
	"city":"New York"
	}
>>> y = json.dumps(x)
>>> print(y)
{"name": "John", "age": 30, "city": "New York"}
>>> print(json.dumps({"name":"John", "age":30}))
{"name": "John", "age": 30}
>>> print(json.dumps(["apple", "bananas"]))
["apple", "bananas"]
>>> print(json.dumps(("apple", "bananas")))
["apple", "bananas"]
>>> print(json.dumps('Hello'))
"Hello"
>>> print(json.dumps(42))
42
>>> print(json.dumps(31.76))
31.76
>>> print(json.dumps(True))
true
>>> print(json.dumps(False))
false
>>> print(json.dumps(None))
null
>>> import json
>>> x = {
	"name":"John",
	"age":30,
	"married": True,
	"divorced": False,
	"children": ("Ann", "Billy"),
	"pets": None,
	"cars": [
		{"model": "BMW 230", "mpg": 27.5},
		{"model": "Ford Edge", "mpg": 24.1}
		]
	}
>>> y = json.dumps(x)
>>> print(y)
{"name": "John", "age": 30, "married": true, "divorced": false, "children": ["Ann", "Billy"], "pets": null, "cars": [{"model": "BMW 230", "mpg": 27.5}, {"model": "Ford Edge", "mpg": 24.1}]}
>>> 
