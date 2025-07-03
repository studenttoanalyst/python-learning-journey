# # Q1. Create a new file named info.txt and write "Learning File Handling in Python" in it.
# try:
#     file = open("info.txt","x")
#     file = file.write("Learning File Handling in Python")
# except FileExistsError:
#     print("File already exists.")
# # Q2. Read and print the contents of info.txt.
# with open("info.txt","r") as file:
#     content = file.read()
#     if content:
#         print("file read!")
#     else:
#         print("file doesn't read!")
#     print(content)

# # Q3. Add the line "Python is powerful!" at the end of info.txt without removing the old content.

# with open("info.txt","a") as file:
#     file.write("\nPython is powerful!")

# # Q4. Create a new file only if it doesn’t exist, otherwise print “File already exists.”

# try:
#     with open("newinfo.txt","x") as file:
#         file.write("this is a new info.txt file")
# except FileExistsError:
#     print("file already exist") 

# Q the game function in a program lets a user play a game and retuurns the score as an integer you
# need to read the file "hi score.txt" which is either blank or contains the previous high score you
# need to write a program to update the high score whenever the game() function breaks the high score

import random
def game():
    print("You are playing game!!!!!")
    score = random.randint(1,65)
    with open("hi score.txt","r") as file:
        highscore = file.read()
        if(highscore != ""):
            highscore = int(highscore)
        else:
            highscore = 0
    print(f"Your score is {score}")
    if(score>highscore):
        with open("hi score.txt","w") as file:
            file.write(str(score))
    return 0

game()








# import random
# def game():
#     print("You are playing game:::::::")
#     score = random.randint(1,66)
#     with open("owaiskifile.txt","r") as file:
#         highscore = file.read()
#         if(highscore != ""):
#             highscore = int(highscore)
#         else:
#             highscore = 0
#     print(f"Your score is {score}")
#     if(score>highscore):
#         with open("owaiskifile.txt") as file:
#             file.write(str(score))
#     return 0
# game()










# import random
# def game():
#     print("You are playing the game")
#     score = random.randint(1,62)

#     with open("hiscore2.txt","r") as file:
#         highscore = file.read()
#         if(highscore != ""):
#             highscore = int(highscore)
#         else:
#             highscore = 0
#     print(f"Your score is {score}")
#     if(score>highscore):
#         with open("hiscore2.txt","w") as file:
#             file.write(str(score))
        
#     return score


# game()





# import random

# def game():
#     print("you are playing the game..")
#     score = random.randint(1, 62)
#     # fetch thhe high score

#     with open("hiscore.txt","r") as file:
#         hiscore = file.read()
#         if hiscore!="":
#             hiscore = int(hiscore)
#         else:
#             hiscore = 0
#     print(f"your score is {score}")
#     if(score>hiscore):
#         # write this hiscore to your file
#         with open("hiscore.txt","w") as file:
#             file.write(str(score))

#     return score


# game() 
