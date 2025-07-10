# EXCEPTIONAL HANDLING
"""In Python, exceptions are errors that stop your program — like dividing by zero or converting text to a number.
To handle these errors without crashing, we use:"""
"""
try:
    # risky code here
except:
    # what to do if error happens
"""

# # Basic syntex
# try:
#     a = int(input("ENter a number: "))
#     b = 10/a
#     print(b)
# except:
#     print("something went wrong!!!!")


# Handling Multiple Excepyions
# try:
#     a = int(input("Enter a: "))
#     b = int(input("Enter b: "))
#     result = a / b
# except ZeroDivisionError:
#     print("Can't divide by zero!")
# except ValueError:
#     print("Please enter valid numbers!")

# # finally: Always Runs
# try:
#     f = open("data.txt")
#     print(f.read())
# except FileNotFoundError:
#     print("File not found!")
# finally:
#     print("Execution complete!")


# # Real Example: Safe Division
# try:
#     num1 = int(input("Enter num1:  "))
#     num2 = int(input("Enter num2:  "))
#     result= num1/num2
# except ZeroDivisionError:
#     print("denomirator must not be zero")
# except ValueError:
#     print("Something went wrong put correct value")
# finally:
#     print("Excecution complete!")

# # Input 2 numbers and an operator (+, -, *, /)
# Handle:
#   - ValueError for invalid number
#   - ZeroDivisionError for /
#   - Handle invalid operator
try:
    num1 = int(input("Enter num1:  "))
    num2 = int(input("Enter num 2: "))
    operator =input(("enter anyone (+,-,*,/): "))
    if operator == "+" or "-" or "*" or "/":
        if operator == "+":
            print(num1 + num2)
        elif operator == "-":
            print(num1 - num2)
        elif operator == "*":
            print(num1 * num2)
        elif operator == "/":
            print(num1/num2)

    else: 

         print("error")
       
except ZeroDivisionError:
    print("zero can not be accepted in denomirator!!")
except ValueError:
    print("Something went wrong!")

