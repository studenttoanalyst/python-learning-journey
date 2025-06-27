#  Python Dictionaries
"""A dictionary is a collection of key-value pairs.
"""
# syntex:
my_dic = {"name":"owais","age":19,"city":"karachi"}
print(type(my_dic))
# accessing values :
print(my_dic["name"])
print(my_dic["age"])
print(my_dic["city"])
# Adding / Updating values
my_dic["name"]="usman" #update
my_dic["country"] = "Pakistan" # add
print(my_dic)
# Removing values
my_dic.pop("name") # remove name key value
print(my_dic)
print(my_dic.keys())
print(my_dic.values())
print(my_dic.items())
print(my_dic.clear())

# Python Sets
"""A set is a collection of unique items."""
# Syntax:
my_set = {1, 2, 3, 4}
# Adding elements
my_set.add(5)
my_set.add("ali")
my_set.add(33.2)
my_set.add(True)
print(my_set)

# Removing elements
my_set.remove(33.2)
my_set.remove("ali")
print(my_set)

# Operations in set theory
set1 = {1,2,3,4,5,6,7,8,9,0}
set2 = {10,11,12,13,14,15,16,17,18,19,20}
print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))

#  What are Conditional Expressions?
"""Conditional expressions are decisions in code.
They check if something is true or false, and then perform some action.
"""