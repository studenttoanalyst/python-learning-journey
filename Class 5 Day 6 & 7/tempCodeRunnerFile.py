# write a program using functions to find greatest of three numbers...
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