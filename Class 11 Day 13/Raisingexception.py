# RAISING EXCEPTION
"""Sometimes you want to manually stop the program and show an error when something is wrong.
This is done using the raise keyword."""
#  Example: Age Validation
# age = int(input("Enter your age:  "))
# if age<0:
#     raise ValueError("age sae put kro..")
# elif age>120:
#     raise ValueError("Age is so high")
# else:
#     print(f"Your age is {age}")

# You can create your own exception class like this:
# class invalidpassword(Exception):
#     pass
# password = input("enter passsword")
# if len(password)<6:
#     raise invalidpassword("Password is too short")
    
# Fixed balance = 5000
# Input withdraw amount.
# # Raise Exception if withdraw amount > balance


# Fixedbalance = 5000
# withdrwa = int(input("Enter amount: "))
# if withdrwa>Fixedbalance:
#     raise Exception("bhai jitna paia h utna nikal ")

# Student Data Validation
# Input name, age, marks.
# Raise different exceptions:
# - Name too short
# - Age out of range
# - Marks not in 0–100

name = input("Enter name:  ")
age = int(input("Enter age:: "))
marks = int(input("enter marks:  "))

if len(name)<5:
    raise Exception("name is too short!!")
elif age>20 or age<0:
    raise Exception("Error in age: !!!")
elif marks>100 or marks<0:
    raise Exception("Marks issue !!11")
else:
    print("Welldone !!!!!!")