# write a program to mine a log file and find out whether it contains "python".
with open("log.txt") as file:
    content = file.read()
if("python" in content):
    print("Yes python is available in content")
else:
    print("No python is not available")