# What is OOP?
# Solving a problem by creating object is one of the most popular approaches in programming
# this is called object oriented progrmming.

# 4 Main Pillars of OOP
# 1_Class: A blueprint/template for creating objects.e.g:: "Car" is a class.
# 2_Object: A real thing created from a class.e.g:: Your Toyota car is an object of Car class.
# 3_Inheritance: Child class can use features of parent class.e.g:: "ElectricCar" inherits from "Car".
# 4_Polymorphism: One thing, many forms — same function behaves differently.e.g::drive() behaves differently in Car and Bike.
# 5_Encapsulation: Keep data safe and private inside the class.e.g:: You can’t directly change bank_balance, only through methods.

# ________________________________________________________________________________________________________________________________


# SYNTEX
class Employee: #CLass
    
    Language = "Py" #Attributes hein ye class k
    salary = 1200000 #Attributes hein ye class k

harry = Employee() #object
harry.name = "Harry"
print(harry.name,harry.Language,harry.salary)

Owais = Employee()
Owais.name = "Owais"
print(Owais.name,Owais.Language,Owais.salary)

# Here names of both employees are object/instance attributes and their languages and salries are the 
# Class attributes as they directed belongs to the class

# NOTE:: instance attributes take preference over class attributes during assignment and retrival