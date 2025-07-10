tableno = int(input("Enter tableno:  "))

table = [tableno*i for i in range(1,11)]
with open("file.txt","a") as file:
    file.write(str(table) + "\n")