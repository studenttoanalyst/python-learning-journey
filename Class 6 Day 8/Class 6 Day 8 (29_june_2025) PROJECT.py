                                   # PROJECT 01

# ROCK,PAPER,SCISSOR GAME

import random

def get_random_value():
    
    return random.choice([1, -1, 0])
"""
1 FOR ROCK
-1 FOR PAPER
0 FOR SCISSOR
"""
Computer = get_random_value()
youstr = input("Enter your choice:  ")
youdic = {"r" : 1 , "p" : -1 , "s" : 0}
reversedic = {1 : "Rock" , -1 : "Paper" , 0 : "Scissor"}
you = youdic[youstr]
print(f"Your choice is {reversedic[you]} and Computer choice is {reversedic[Computer]}")
if( you == Computer):
    print("Draw!!!!!!!")
else:
    if(Computer == 1 and you == -1):
        print("You Win!")
    elif(Computer == 1 and you == 0):
        print("you Lose!")
    elif(Computer == -1 and you == 0):
        print("you Win!")
    elif(Computer == -1 and you == 1):
        print("you Lose!")
    elif(Computer == 0 and you == -1):
        print("you Lose!")
    elif(Computer == 0 and you == 1):
        print("you Win!")
    else:
        print("Something went wrong")
    