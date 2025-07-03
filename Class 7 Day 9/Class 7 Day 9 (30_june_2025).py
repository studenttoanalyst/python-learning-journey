# # FILE INPUT/OUTPUT IN PYTHON
# # What is File I/O in Python?
# """It means reading data from a file (Input) and writing data to a file (Output).
# We use this when we want to save data permanently or read data that’s already saved."""

# #  Basic Steps
# #  1. Open the file
# file = open("filename.txt", "mode")
# """"filename.txt" = name of the file
# "mode" = how you want to use it:
# "r" → read
# "w" → write
# "a" → append
# "x" → create new file
# "r+" → read and write
# """

# # 2. Read or Write  
# # Reading from file
# data = file.read()
# print(data)
# # Writing to file
# file.write("Hello, this is a test.")
# # 3. Close the file
# file.close()

# Example 01 (Write to a file)
file = open("myfile.txt","w")
file.write("Hello,Python Developers")
file.close()

# Example 01 (Read from a file)
# file = open("myfile.txt")
# content = file.read("owais you are their?")
# print(content)
# file.close()

# Append (Add) to a File
with open("myfile.txt","a") as file:
    file.write("\nHow are you?")

#  Shortcut: with open() – Automatically closes file
with open("myfile.txt", "r") as file:
    data = file.read()
    print(data)

# try:   
#    with open("owais.txt","x") as owais:
#     owais.write("This is new file")
# except FileExistsError:
#      print("File already exists.")


# with open("owais.txt","r") as owais:
#     print(owais.read())



