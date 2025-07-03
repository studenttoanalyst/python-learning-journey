# write  a program to find out whether a file is identical & matches the content of another file
with open("this.txt","r") as file:
    content = file.read()
with open("thiscopy.txt","r") as file:
    content2=file.read()
if(content==content2):
    print("Yes botha re same")
else:
    print("No both are not same")
