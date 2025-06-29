# LISTS AND TUPLES
# Q1 write a program to store 7 fruits in a list entered by the user
fruits = []
f1 = input("ENter fruite name: ")
fruits.append(f1)
f2 = input("ENter fruite name: ")
fruits.append(f2)
f3 = input("ENter fruite name: ")
fruits.append(f3)
f4 = input("ENter fruite name: ")
fruits.append(f4)
f5 = input("ENter fruite name: ")
fruits.append(f5)
f6 = input("ENter fruite name: ")
fruits.append(f6)
f7 = input("ENter fruite name: ")
fruits.append(f7)
print(fruits)

# Q2 write a program to accept 6 students marks and displayed them in a shorted manner
marks = []
m1 = int(input("ENter marks : "))
marks.append(m1)
m2 = input("ENter marks : ")
marks.append(m2)
m3 = input("ENter marks : ")
marks.append(m3)
m4 = input("ENter marks : ")
marks.append(m4)
m5 = input("ENter marks : ")
marks.append(m5)
m6 = input("ENter marks : ")
marks.append(m6)
print(marks)

#Q3 Check that tuple type cannot be changed in python
a = (1,2,"alo")
a["alo"] = 44 # tuple cannot be changed

# Q4 write a program to sum a list with four numbers
list = [1,2,3,4,]
print(sum(list))

# q5 write a program to count zeros in the following tuple:
tuple = (1,2,0,9,0,4)
n = tuple.count(0)
print(n)