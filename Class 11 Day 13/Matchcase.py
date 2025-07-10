# MATCH CASE
"""match-case is like a switch statement in other languages.
It was introduced in Python 3.10.
It helps you write clean and readable conditional code when you want to check multiple cases.
"""

# value = input("Enter a fruit: ")

# match value:
#     case "apple":
#         print("You chose apple.")
# #     case "banana":
# #         print("You chose banana.")
# #     case "mango":
# #         print("You chose mango.")
# #     case _:
# #         print("Unknown fruit.")

# # Match with Multiple Options:
# color = input("Enter a color: ")

# match color:
#     case "red" | "blue" | "green":
#         print("Primary color")
#     case "yellow" | "pink":
#         print("Secondary color")
#     case _:
#         print("Unknown color")


# # Match with Conditions (Advanced):
# num = int(input("Enter a number: "))

# match num:
#     case _ if num > 0:
#         print("Positive number")
#     case _ if num < 0:
#         print("Negative number")
#     case _:
#         print("Zero")

# Day of the Week
# day = input("Enter day:  ")

# match day:
#     case "Monday":
#         print("Moanday is the first day of a week")
#     case "Tuesday":
#         print("Tuesnday is the second day of a week")
#     case "Wednesday":
#         print("Wednesday is the third day of a week")
#     case "Thursday":
#         print("Thursday is the fourth day of a week")
#     case "Friday":
#         print("Friday is the fifth day of a week")
#     case "Saturday":
#         print("saturday is the first day of a week")
#     case "Sunday":
#         print("sundayday is the first day of a week")
#     case _:
#         print("bla bla!!")

# Vowel or Consonant
# Input: a single letter
# Use match to check if it's a vowel (a, e, i, o, u)

# Letter = input("Enter a letter:  ")
# match Letter:
#     case "a"|"A":
#         print("a is a vowel")
#     case "e"|"E":
#         print("e is a vowel")
#     case "i"|"I":
#         print("i is a vowel")
#     case "o"|"O":
#         print("o is a vowel")
#     case "u"|"U":
#         print("u is a vowel")
#     case _:
#         print("consonants")


# Basic Calculator
# Input two numbers and an operator (+, -, *, /)
# Use match to perform the operation
# n1 = int(input("Enter a number:  "))
# n2 = int(input("Enter a number:  "))
# operator = input("enter operation + - * /:  ")

# match operator:
#     case "+":
#         print(n1 + n2)
#     case "-":
#         print(n1 - n2)
#     case "*":
#         print(n1 * n2)
#     case "/":
#         if n2==0:
#             print("undefined")
#         else:
#             print(n1/n2) 
#     case _:
#         print("Something went wrong!!!!!!!!")


# Number Sign
# Input a number
# Use match with condition: if positive, negative, or zero

# number = int(input("Enter a num:  "))
# match number:
#     case _ if number>0:
#         print("Positive")
#     case _ if number<0:
#         print("negative")
#     case _:
#         print("Zero")

# use role checker
# Input: "admin", "user", "guest"
# Print different messages for each role

Role = input("Enter role guest,admin or user:  ")
match Role:
    case _ if Role == "admin":
        print("I m admin")
    case _ if Role == "user":
        print("I m user")
    case _ if Role == "guest":
        print("I m guest")
    case _:
        print("Something went wrong!!!!")