# STRINGS
'''string is a datatype in python
it is a sequence of character encloused in quotes'''
# we can primarily write a strings in these three ways:
'''a  = "owais"
   b = 'owais'
   c = \'''owais\''' '''
# STRING SLICING 
'''A STRING IN A PYTHON 
CAN BE 
SLICED FOR GETTING A PART OF THE STRINGS'''
sli = name[ind_strt:ind_end]
# List in Python
'''A list is a changeable (mutable) collection that can store multiple values like numbers, strings, etc.'''
# Syntax:
'''my_list = [10, 20, "hello", True]
'''
# Features:
'''Can change values

Can add or remove items

Can contain mixed data types

Ordered (items keep their position)'''
# Example:
'''fruits = ["apple", "banana", "mango"]
print(fruits[0])        # apple
fruits[1] = "orange"     # change value
print(fruits)           # ['apple', 'orange', 'mango']
'''
# List Slicing
'''nums = [10, 20, 30, 40, 50]
print(nums[1:4])     # [20, 30, 40]
print(nums[::-1])    # Reverse list: [50, 40, 30, 20, 10]
'''
# List Methods
''''''
# Tuple in Python
'''A tuple is like a list, but it is unchangeable (immutable) — you cannot change the values once it's created.'''
# Syntax
'''my_tuple = (10, 20, "hello", True)
'''
# Features
'''Cannot change or modify

Uses round brackets ()

Often used for fixed data

Also ordered'''
# Example
'''colors = ("red", "green", "blue")
print(colors[0])         # red
# colors[1] = "yellow"   ❌ This will cause an error
'''
# Converting Between List & Tuple
'''my_list = [1, 2, 3]
my_tuple = tuple(my_list)

print(my_tuple)  # (1, 2, 3)

back_to_list = list(my_tuple)
print(back_to_list)  # [1, 2, 3]
'''