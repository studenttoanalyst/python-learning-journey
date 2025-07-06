# MULTILEVEL INHERITANCE
"""WHEN A CHILD CLASS BECOME A PARENT CLASS FOR ANOTHER CHILD CLASS"""

# class Employee:
#     company = "Microsoft"
#     name = "Owais"
#     salary = 129999
#     language = "Python"
#     def show(slef):
#         print(f"""The company name is {slef.company}
#                  The name of Employee is {slef.name}
#                  The language is {slef.language}
#               and his salary is {slef.salary}""")
        
# class Programmer(Employee):
#      company = "Google"
#      name = "ASad"
#      language = "javascript"
#      salary = 1300000
#      def show(slef):
#         print(f"""The company name is {slef.company}
#                  The name of Employee is {slef.name}
#                  The Language is {slef.language}
#               and his salary is {slef.salary}""")
        
# class Manager(Programmer):
#      company = "Google"
#      name = "ASad"
#      language = "javascript"
#      salary = 1300000
#      def show(slef):
#         print(f"""The company name is {slef.company}
#                  The name of Employee is {slef.name}
#                  The Language is {slef.language}
#               and his salary is {slef.salary}""")

# o = Manager()
# print(o.company)

class Employee:
    a = 1
class Programmer(Employee):
    b = 2
class Manager(Programmer):
    c = 3

o = Employee()
print(o.a) # prints the a attribute
# print(o.b) # shows an eror because as there is no b attribute in EMployee class

o = Programmer()
print(o.a , o.b)

o = Manager()
print(o.a,o.b,o)
print(o.b + o.c + o.a)