# write a list comprehension to print a list which contains the multiplication table of a user entered number

tableno = int(input("Enter tableno:  "))

table = [tableno*i for i in range(1,11)]
print(table)