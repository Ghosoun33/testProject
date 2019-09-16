Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:13:57) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> i = 1
>>> while i < 6:
	print(i)
	i += 1

	
1
2
3
4
5
>>> i = 1
>>> while i < 6:
	print(i)
	if i == 3:
		break
	i += 1

	
1
2
3
>>> i = 0
>>> while i < 6:
	i += 1
	if i == 3:
		continue
	print(i)

	
1
2
4
5
6
>>> i = 1
>>> while i < 6:
	print(i)
	i += 1
else:
	print('i is no longer less than 6')

	
1
2
3
4
5
i is no longer less than 6
>>> i = 1
>>> while i < 10:
	print(i)
	i += 1
else:
	print('i is no longer less than 10')

	
1
2
3
4
5
6
7
8
9
i is no longer less than 10
>>> 
