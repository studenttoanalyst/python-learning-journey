# Loops in python
# Q1 write a program to print multiplication table of a given num by user.
tableno = int(input("Enter table no:  "))
for i in range(1,11):
    print(f"{tableno} X {i} = {tableno*i}")

# Q2 attempt problem 1 using while loop
tableno = int(input("Enter table no:  "))
i = 1
while(i<11):
    print(f"{tableno} X {i} = {tableno*i}")
    i +=1
   
# Q3 write a program to greet all person name stored in a list l and which starts with s
l =["sahil","ali","subhan","basit"]
for name in l:
    if(name.startswith("s")):
        print("hello!",name.capitalize() + "!") 

# Q4 write a program whether a number is prime or not
num = int(input("enter a num: "))
if(num<0):
    print("please put positive num")
else:
    for i in range(2,num):
        if(num%i==0):
            print("number is not prime!")
            break
        else:
            print(f"its a prime number {i}")

# Q5 write a program to find the sum of first n natural numbers usimg while loop.
n = int(input("Enter a number: "))
i = 1
sum = 0
while(i<=n):
    sum += i
    i+=1
print(f"the sum first {n} natural number is {sum}")

# Q6 write a program to find the factorial of given  number by user using for loop.
n = int(input("Enter a number: "))
factorial = 1
for i in range(1,(n+1)):
    factorial *= i
print(f"The factorial of {n} number is {factorial}")

# Q7 write a program to print the following star pattern:
"""
  *
 ***  for n = 3
*****
# """
n = int(input("Enter a num: "))
for i in range(1,n+1):
    print(" "* (n-i),end="")
    print("*"*(2*i-1),end="")
    print("\n")
# Q8 write a program to print the following star pattern:
"""
*
**  for n = 3
***
"""
n= int(input("Enter a num: "))
for i in range (1,n+1):
    print("*"*i,end="")
    print("")

# Q9 write a program to print the following star pattern:
"""
***
* *       for n = 3
***
"""

n= int(input("Enter a num: "))
for i in range (1,n+1):
    if(i==1 or i==n):  
      print("*"*n,end="")
    else:
       print("*",end="")
       print(" "*(n-2),end="")
       print("*",end="")
    print()

# Q10 write a program to print multiplication table of n using for loops in reversed order.
tableno = int(input("Enter table no: "))
for i in range(1,11):
    print(f"{tableno} X {11-i} = {tableno*(11-i)}")
