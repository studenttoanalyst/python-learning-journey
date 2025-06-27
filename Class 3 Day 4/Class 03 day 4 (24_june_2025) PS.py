# Q1 Create a dictionary that stores:name,age,city
"""Print only the name , upadate age to 21 , addd country """
my_dic = {
    "name" : "owais",
    "age"  : 18 ,
    "city" : "karachi"
}
print(my_dic)
print(my_dic["name"])
my_dic["age"]=21
my_dic["Country"]="Pakistan"
print(my_dic)


#  Question 2: Simple Product Price Update You have this dictionary:
product = {
    "item":"pen",
    "price": 36
}
"""Print the price,Increase price to 35,Add a new key "stock": 50"""

print(product["price"])
product["price"] = 35
print(product)
product["stock"] = 50
print(product)

# Question 3: Remove a Key
person = {
    "name": "Ali",
    "gender": "Male",
    "city": "Lahore"
}
# Remove "city" and print updated dictionary.
# solution
person.pop("city")
print(person)

# SET PRACTICE
# Question 2: Add & Remove Values in Set
users = set()
"""Add "Ali", "Ayesha"
 Then remove "Ali" and print final set"""
users.add("ali")
users.add("Ayesha")
print(users)
users.remove("ali")
print(users)

# Question 3: Set Operations
a = {1, 2, 3}
b = {3, 4, 5}
""" Find:

Union

Intersection

Difference (a - b)"""

print(a.union(b))
print(a.intersection(b))
print(a.difference(b))

# Conditional Expressions  Practice Questions
# Q1: Check if a number is positive or negative (if-else)

number = -5
if(number>0):
    print("\nthe number is positiove ")
elif(number==0):
    print("\nthe number is 0")
else:
    print("\nthe number is negative")

#  MINI PROBLEM 1: Movie Ticket Price
"""A cinema charges:
Rs. 500 if age < 18
Rs. 800 if age ≥ 18""" 

age = 15

if(age<18):
    print("\nthe price of ticket is: RS 500")
elif(age>=18):
    print("\nthe price of ticket is: RS 800")
else:
    print("\nError!")

# MINI PROBLEM 2: Login System
"""👤 Ask user for username and password.
Only allow login if:
username == "admin"
password == "12345"""

username = "admin"
password = 1234321
if(username == "admin" and password == 12345):
    print("\nallowed")
else:
    print("\nnot allowed")