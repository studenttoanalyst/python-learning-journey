# PROJECT 2 (THE PERFECT GUESS)
"""WE ARE GOING TO WRITE A PROGRAM THAT GENERATES A RANDOM NUMBER AND ASK THE USER TO GUESS IT
   IF THE PLAYER GUESS IS HIGHER THAN THE ACTUAL NUMBER,THE PROGRAM DISPLAYS "LOWER NUMBER PLEASE"
   SIMILARLY IF THE USER GUESS IS TOO LOW.THE PROGRAM PRINTS 'HIGHER NUMBER PLEASE' WHEN THE USERS
   GUESSES THE CORRECT NUMBER,THE PROGRAM DISPLAYS THE NUMBER OF GUESSES THE PLAYER USED TO ARRIVE AT THE NUMBER"""


import random
n = random.randint(1,100)
a = -1
guesses = 0
while(a!=n):
    guesses += 1
    a = int(input("Guess a Number between 1 and 100:  "))
    if(a>n):
        print("Lower number please!!!")
    elif(a<n):
        print("Higher number please!!!")
    else:
        print("Good job")
    
print(f"You have guessed the number {n} correctly in {guesses} attempts")
















# import random
# n = random.randint(1,100)
# a = -1
# guesses = 0
# while(a!=n):
#     guesses += 1
#     a = int(input("Enter the guess:  "))
#     if(a > n):
#         print("Lower number please!!!")
#     else:
#         print("Higher number please!!!")

# print(f"You have guessed the number {n} correctly in {guesses} attempt ")