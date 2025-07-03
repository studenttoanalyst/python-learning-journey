# Repeat program 4 for a list of such words to be censord

words = ["donkey","bad","ganda"]
with open("file.txt") as file:
    content = file.read()

for word in words:
    content = content.replace(word,"#####")

with open("file.txt","w") as file:
    file.write(content)