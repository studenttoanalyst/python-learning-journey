# write a program to read a text from a given file(poems.txt) and find out whether it contains the word twinkle
with open("poem.txt") as file:
    content = file.read()

if("twinkle" in content):
    print("Yes twinkle is available!!")
else:
    print("No ")
