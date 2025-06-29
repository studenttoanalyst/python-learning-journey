# DICTIONARY AD SETS
# Q1 write a program to create a dictionary of hidi words translate into english

Words = {
    "kursi" : "chair",
    "billi" : "cat",
    "pani" : "water"
}
print(Words)

# Q2 write a program to input eight numbers from the users and display all unique numbers at once
s = set()
n = input("Ennter number: ")
s.add(int(n))
n = input("Ennter number: ")
s.add(int(n))
n = input("Ennter number: ")
s.add(int(n))
n = input("Ennter number: ")
s.add(int(n))
n = input("Ennter number: ")
s.add(int(n))
n = input("Ennter number: ")
s.add(int(n))
n = input("Ennter number: ")
s.add(int(n))
n = input("Ennter number: ")
s.add(int(n))

print(s)

# Q3 can we have a set with 18(int) and '18'(str) as a value in it?

s = set()
nXint = 18
nXstr = "18"
s.add(nXint)
s.add(nXstr)
print(s)
# yes we can have a set with 18(int) and '18'(str)

# Q4 what will be the length of following set s?
s = set()
s.add(20)
s.add(20.0)
s.add('20') # length of s after this operation
print(s)
print(len(s))

# Q5 what is the type of s?
s = {}
print(type(s))

# Q6 Create an empty dictionary allow four friends to enter their favourite language as value and use key as their name assumes that the names are unique
dic = {} 
name = input("Enter name: ")
language = input("enter language: ")
dic.update({name:language})
name = input("Enter name: ")
language = input("enter language: ")
dic.update({name:language})
name = input("Enter name: ")
language = input("enter language: ")
dic.update({name:language})
name = input("Enter name: ")
language = input("enter language: ")
dic.update({name:language})
print(dic)

# Q7 can you change the values inside a list which is contained in set s?
s = {8,7,12,"harry",[1,2]}
# We never include a list in a set
# sets are immutable