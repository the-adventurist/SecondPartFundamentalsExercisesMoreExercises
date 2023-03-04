from operator import getitem

test_dict = {'Nikhil' : { 'roll' : 24, 'marks' : 17},
             'Akshat' : {'roll' : 54, 'marks' : 12},
             'Akash' : { 'roll' : 12, 'marks' : 15}}

sorted_test_dict = {name: sorted(value.items(), key=lambda el: el[1], reverse=True) for name, value in test_dict.items()}

print(sorted_test_dict)

# Python3 code to demonstrate
# Sort nested dictionary by key
# using OrderedDict() + sorted()
from collections import OrderedDict
from operator import getitem

# initializing dictionary
test_dict = {'Nikhil' : { 'roll' : 24, 'marks' : 17},
			'Akshat' : {'roll' : 54, 'marks' : 12},
			'Akash' : { 'roll' : 12, 'marks' : 15}}

# printing original dict
print("The original dictionary : " + str(test_dict))

# using OrderedDict() + sorted()
# Sort nested dictionary by key
res = sorted(test_dict.items(),
	key = lambda x: getitem(x[1], 'marks'))

# print result
print("The sorted dictionary by marks is : " + str(res))
