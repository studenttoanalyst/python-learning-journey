# SUPER() METHOD
"""Super method is used to access the methods of a super class in a derived class"""

class Employee:
    def __init__(self):
        print("This is the constructor of Employee Class")
    a = 1
        # print(a)
class Programmer(Employee):
    def __init__(self):
        super().__init__()
        print("This is the constructor of Programmer Class")
    b = 2
        # print(b)
class Manager(Programmer):
    
    def __init__(self):
        super().__init__()
        print("This is the constructor of Manager Class")
    c = 3

   
# o = Employee()
# print(o.a) # prints the a attribute
# # # print(o.b) # shows an eror because as there is no b attribute in EMployee class

# o = Programmer()
# print(o.a , o.b)

o = Manager()
print(o.a,o.b,o)
print(o.b + o.c + o.a)
