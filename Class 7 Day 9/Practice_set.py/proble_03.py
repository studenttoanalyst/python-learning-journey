# Write a program to renamed a file
with open("oldfile.txt","r") as file:
    content = file.read()
with open("newfile.txt","w") as file:
    file.write(content)