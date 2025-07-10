# Q write a program to open three files 1.txt,2.txt,3.txt if any these files are not presetb a message without exiting the program
# must be printed prompting teh same
try:
    with open("1.txt","r") as file:
        print(file.read())
except:
    print("Their is no file")
try:
    with open("2.txt","r") as file:
        content = file.read()   
        print(content)
except:
    print("Their is no file")
try:
    with open("3.txt","r") as file:
        print(file.read())
except:
    print("Their is no file")