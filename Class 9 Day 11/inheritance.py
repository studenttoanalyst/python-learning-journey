# Inheritance is a way of creating a new class from an existing class
#  TYPES OF INHERITANCE 
# Single inheritance
# Multiple inheritance
# Multilevel inheritance
# _________________________________________________________________________

# SINGLE INHERITANCE
"""Single inheritance occurs when child class inherites only a single parent class"""

class Employee:
    company = "ITC"
    name = "owais"
    salary = 122
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")


# class Programmer:
#     company = "ITC infotech"
#     def show(self):
#         print(f"The name is {self.name} and the salary is {self.salary}")
    
#     def showlanguage(self):
#         print(f"the name is {self.name} and the good with {self.language} language")

class Programmer(Employee):
    company = "ITC infotech"
    def showlanguage(self):
        print(f"the name is {self.name} and the good with {self.language} language")

a = Employee()
b = Programmer()
print(a.company,b.company)
a.show()
 
