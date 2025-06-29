# # STRINGS
# # Q1 write a python program to display a user entered name followed by good afternoon using input function
# name = input("Enter user name :  ")
# print(f"Good Afternoon {name}") 

# # Q2 write a program to fill in aletter template given below with name and date:

# letter = """
#            Dear <|Name|>,
#            Your are selected!
#            <|Date|>    
# """
# print(letter.replace("<|Name|>","Owais").replace("<|Date|>","29_June_2025"))

# Q3 Write a program to detect double space in a string

string = "hello owais  how are you?"
print(string.find("  "))

# Q4 replace the double space from single space in problem 3

print(string.replace("  "," "))

# Q5 Write a program to format the following letter using escape sequence characters.

letter = "Dear Owais,\n\tThis python course is nice,\nThanks"
print(letter)