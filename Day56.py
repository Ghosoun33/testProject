Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
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
>>> print(json.dumps(x, indent=4))
{
    "name": "John",
    "age": 30,
    "married": true,
    "divorced": false,
    "children": [
        "Ann",
        "Billy"
    ],
    "pets": null,
    "cars": [
        {
            "model": "BMW 230",
            "mpg": 27.5
        },
        {
            "model": "Ford Edge",
            "mpg": 24.1
        }
    ]
}
>>> print(json.dumps(x, indent=4, separators=(". ", " = ")))
{
    "name" = "John". 
    "age" = 30. 
    "married" = true. 
    "divorced" = false. 
    "children" = [
        "Ann". 
        "Billy"
    ]. 
    "pets" = null. 
    "cars" = [
        {
            "model" = "BMW 230". 
            "mpg" = 27.5
        }. 
        {
            "model" = "Ford Edge". 
            "mpg" = 24.1
        }
    ]
}
>>> print(json.dumps(x, indent=4, sort_keys=True))
{
    "age": 30,
    "cars": [
        {
            "model": "BMW 230",
            "mpg": 27.5
        },
        {
            "model": "Ford Edge",
            "mpg": 24.1
        }
    ],
    "children": [
        "Ann",
        "Billy"
    ],
    "divorced": false,
    "married": true,
    "name": "John",
    "pets": null
}
>>> 
