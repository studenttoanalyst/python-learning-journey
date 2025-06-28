# # Functions
# """A function is a groupp of statements to performing a specofoc tasks"""
# # syntex
# # Function Definition
# def func1():
#     print("hello world")
# # calling function
# func1()

# def average():
#     a = int(input("enter a number"))
#     b = int(input("enter a number"))
#     c = int(input("enter a number"))

#     average = (a+b+c)/3
#     print(average)

# average()


# Quik Quiz write a code to greet a user with "Good day " using functions


def greet(name,ending):
        print("Good day " + name)  # added space after "Good day"
        print(f"{ending}")

greet("owais","thank you")

# return function
def average(a, b, c):
    return (a + b + c) / 3

avg = average(1, 2, 3)
print(avg)

# Default parameter value
def greett(name,ending="thank you"):
      print("Good day " + name)
      print(ending)

greett("harry")  
# Recursion is  a function which calls its self
"""Example
"""
# find factorial of a number 
def factorial(n):
    if(n==1 or n==0):
        return 1
    return n*factorial(n-1)

n = int(input("enter a number"))
print(f"the factorial of {n} is {factorial(n)}")