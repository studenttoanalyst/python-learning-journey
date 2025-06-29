# FUNCTIONS AND RECURSION
# Q1 Write a program using functions to find greatest of three numbers
def greatest(a,b,c):
    if(a==b==c):
        print("All numbers are same")
    else:
        if(a>b and a>c):
            print(f"The greatest no is {a}")
        elif(b>a and b>c):
            print(f"The greatest no is {b}")
        elif(c>a and c>b):
            print(f"The greatest no is {c}")
        else:
            print("Some thing went wrong!")

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
num3 = int(input("Enter a number: "))

greatest(num1,num2,num3)

# Q2 write a recursive function to calculate the sum of first n natural numbers.

"""
sum of first n natural number
sum(1)=1
sum(2)=1+2
sum(3)=1+2+3
sum(4)=1+2+3+4
sum(5)=1+2+3+4+5
sum(n)=1+2+3+...............+n
sum(n)=sum(n-1)+n
"""
def sum(n):
    if n==1:
        return 1
    elif n<1:
        return 0
    else:
      return sum(n-1)+n
    
n = int(input("Enter a num: "))
print(f"The sum of {n} natural numbers is {sum(n)}")

# Q3 write a python program to print this pattern by using functions:
"""
***
**  for n=3
*
"""

def pattern(n):
    if n==0:
        return
    print("*" * n)
    pattern(n-1)

pattern(5)

# Q4 write a python program to print inch to cm using functions
def inch_to_cm(inch):
    return inch*2.54

inch = int(input("Enter a num: "))
result = inch_to_cm(inch)
print(f"the conversion from {inch} to cm is {result}")

# Q5 write a python function to print multiplication table
def table(n):
    for i in range(1,11):
        print(f"{n} X {i} = {n*i}")
    
tableno = int(input("Enter a table no: "))
table(tableno)
