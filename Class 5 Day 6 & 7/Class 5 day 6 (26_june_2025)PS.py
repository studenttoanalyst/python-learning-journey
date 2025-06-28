# # write a program using functions to find greatest of three numbers...
# def greatest(a,b,c):
#     if(a>b and a>c):
#         print("the greatest number is a")
#     elif(b>a and b>c):
#         print("the greatest number is b")
#     elif(c>b and c>a):
#         print("the greatest number is c")

# a = int(input("Enter a num"))
# b = int(input("Enter a num"))
# c = int(input("Enter a num"))

# result = greatest(a,b,c)
# print(f"the greatest no is {result}")

# # write a python program using function to convert celsius to fahrenheit....
# # c = 5*(f-32)/9

# def C_to_F(c):
#     return (c*9/5)+32

# c = int(input("eneter a number"))

# result = C_to_F(c)
# print(f"the celsius to f is {result}")

# # write a recursion function to calculate the sum of first n natural numbers
# """
# sum(1) = 1
# sum(2) = 1  + 2
# sum(3) = 1  + 2 + 3
# sum(4) = 1  + 2 + 3 + 4
# sum(5) = 1  + 2 + 3 + 4 + 5

# sum(n) = 1 + 2 + 3  + .................. + (n-1)     + n
# sum(n) = sum(n-1) + n
# """

# def sum_of_natural_numbers(n):
#     if(n==1):
#        return 1
#     return sum_of_natural_numbers(n-1) + n

# a = int(input("enter a num for sum"))
# Sumof_n_numbers = sum_of_natural_numbers(a)

# print(Sumof_n_numbers)

# write a python function to print first n lines of the following patterns:
"""
***
**                        for n = 3
*
"""

# def pattern(n):
#     if(n==0):
#         return
#     print("*" * n)
#     pattern(n-1)

# n = int(input("enter no for patternn"))
# # pattern(n)

# def pattern(n):
#     if(n==0):
#         return
#     print("*"*n)
#     pattern(n-1)

# n = int(input("enter a num for print pattern"))
# pattern(n)

# # write a python functions which converts inchs to cms
# def inc_to_cms(inch):
#     return inch * 2.54

# inch = int(input("enter inchs "))

# print(f"this is the conversion from inchs{inch} to cms{inc_to_cms(inch)}")

# write a python function to print multiplication table of a given number
def table(n):
    for i in range(1,11):
        print(f"{n} X {i} = {n*i}")
    
n = int(input("enter a table no"))
table(n)