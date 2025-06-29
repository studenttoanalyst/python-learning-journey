# CONDITIONAL EXPRESSIONS
# Q1 write a program to find greatest of four numbers entered by user
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
num3 = int(input("Enter a number: "))
num4 = int(input("Enter a number: "))
if(num1==num2==num3==num4):
    print("All NUMBERS ARE EQUAL")
else:
        if(num1>num2 and num1>num3 and num1>num4):
           print(f"The greatest number among them is {num1}")
        elif(num2>num1 and num2>num3 and num2>num4):
           print(f"The greatest number among them is {num2}")
        elif(num3>num2 and num3>num1 and num3>num4):
           print(f"The greatest number among them is {num3}")
        elif(num4>num2 and num4>num3 and num4>num1):
           print(f"The greatest number among them is {num4}")
        else:
           print("Some thing went wrong!!!")

# Q2 write a program to findout whether a student has passed or failed if it requires a total of
# 40% and at least 33% in eah subject to pass assume 3 subjects and takes marks as input from user

subject1 = int(input("Enter your marks: "))
subject2 = int(input("Enter your marks: "))
subject3 = int(input("Enter your marks: "))
if(subject1>100 or subject2>100 or subject3>100):
    print("Some thing went wrong!!!!!")
else:
    if(subject1<33 or subject2<33 or subject3<33):
        print(f"Your percentage in each subject is less than 33 therefore you fail!!")
    else:
        average = (subject1+subject2+subject3)/3
        if(average<40):
            print("You have failed b/c your total percentage is less than 40%")
        else:
            print("Congratulations you have passed!")


# Q3 A spam comment is defined as a text containning  following keywords: 
"""
make a lot f money,buy now,subscribe this , click now
"""
p1 = "Make a lot of money"
p2 = "Buy now"
p3 = "Now subscribe"
p4 = "Click now"

Message = input("Enter th message: ")

if(Message == p1 or Message == p2 or Message == p3 or Message == p4):
    print("This message is spam!!!")
else:
    print("This message is not spam...")

# Q4 write a program to find whether a given username contain less than 10 characters or not
Username = input("ENTER USERNAME:  ")
if(len(Username)<10):
    print("Yes it contain less than 10 characters...")
else:
    print("No its not contain less than 10 characters!")

# Q5 write a program which find out whether a given name is present in list or not

list = ["owais","umair","asad","faizan","aftab"]
Name = input("Enter your name:  ")
if(Name in list):
    print("Yes it is available in list!!")
else:
    print("its not availabe!")

# Q6 write a program to calculate the grade of a student from his marks from the following scheme.
"""90_100 = Ex
   80_90 = A
   70_80 = B
   60_70 = C
   50_60 = D
   <50 = F 
    """
marks = int(input("Enter your marks:  "))
if(marks>100 or marks<0):
    print("Something went wrong!!!")
else:    
    if(marks>90 and marks<=100):
        print("Ex")
    elif(marks>80 and marks<=90):
        print("A")
    elif(marks>70 and marks<=80):
        print("B")
    elif(marks>60 and marks<=70):
        print("C")
    elif(marks>=50 and marks<=60):
        print("D")
    else:
        print("F")

# Q7 write a program to find out whether a given post is talking about harry or not?
post = input("Enter a post: ")

if("harry" in post.lower()):
    print("Yes! it is available in this post")
else:
    print("its not available")