# NEWLY ADDED FEATURES IN PYTHON
# 1__Walrus Operator
"""The walrus operator (:=) introduced in python3.8 allows you to asign values to variables as part of an expression.This operators
resemblance to the eyes and tusks of a walrus,is officially called the 'Assignment expression' """
# Example
# -> without walrus method
# n = int(input("Enter a number:  "))
# while n!=0:
#     print(f"You Entered {n}")
#     n = int(input("Enter a number:  "))

# # -> with walrus method
# while(n := int(input("Enter a number: "))) != 0:
#     print(f"You entered: {n}")


# # Another Example
# # -> without walrus method
# name = input("Enter a number:  ")
# if len(name) > 3:
#     print(f"Your name has {len(name)} letters")

# # # -> with walrus method
# if(length := len(input("Enter your name:  "))) > 3:
#     print(f"Your name has {length} letters ")


# now practice 
# # print a program in which we sae that which is great among a and b withh or without walrus operator
# # -> without walrus method
# a = int(input("Enter num a:  "))
# b = int(input("Enter num b:  "))
# if a>b:
#     print(f"The value of a {a} is greater than b {b} ")
# elif b>a:
#     print(f"The value of b {b} is greater than a {a} ")
# # else:
# #     print("Both numbers are same")
# # # # -> with walrus method
# if(a := int(input("Enter the value of a"))) > (b := int(input("Enter num b:  "))) > a:
#   print(f"The value of a {a} is greater than b {b} ")
# elif b>a:
#        print(f"The value of b {b} is greater than a {a} ")

# else:
#     print("Both are same")




# Use walrus to take a number and print if it's even or odd.
# first we will do it without walrus operators
 
# num = int(input("Enter a num:  "))

# if(num%2==0):
#     print(f"The num {num} is Even")
# else:
#     print(f"The number {num} is odd number")

# # with walrus operator
# if(num := int(input("Enter a num:  ")))%2==0:
#         print(f"The num {num} is Even")
# else:
#             print(f"The number {num} is odd number")




"""Keep taking integers from the user and calculate the sum until
 the user enters a negative number. Use walrus inside a while loop."""

# # First we do it wothout walrus operator
# n = int(input("Enter an integer:  "))
# i = 0
# while (n!=0):
#     print(n)
#     i +=    1
#     n = int(input("Enter an integer:  "))
# print(f"You entered {i} non-zero numbers.")

# with walrus operator
# i=0
# while(n := int(input("Enter a num:  "))) != 0:
#     print(n)
#     i+=1
# print(f"You entered {i} non-zero numbers.")

"""Ask for passwords until user enters a password with at least 8 characters"""

# # First do it without walrus operator
# Password = input("Enter password:  ")
# if(len(Password)>=8):
#     print(f"You entered {len(Password)} digits password")
# else:
#     print("Incorrect opss !!!!!!")

# With walrus operator
if ( Password := len(input("Enter password:  "))) >= 8:
     print(f"You entered {Password} digits password")
else:
     print("Incorrect opss !!!!!!")