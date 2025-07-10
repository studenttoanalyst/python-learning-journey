# write a program to input name,marks and phone number of a student and format it using the  format function like below:
"""The name of the student is harry,his marks ARE 72 and phone number is 4444444"""

name = input("ENter name:  ")
marks = int(input("Enter marks: "))
number = int(input("enter phone:  "))
s = "The name of the student is {name},his marks ARE {marks} and phone number is {number}".format
(name,marks,number)


print(s)