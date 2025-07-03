# Q Creating a class "programmer" for storing information of few programmers working at home

# class programmers:
#     Company = "Microsoft"
#     def __init__(self,name,salary,pin):
#         self.name = name
#         self.salary = salary
#         self.pin = pin
    
# p = programmers("Harry",120000,1234)
# print(p.name,p.Company,p.salary,p.pin)
# r = programmers("rohan",120000,1234)
# print(r.name,r.Company,r.salary,r.pin)
# s = programmers("sami",120000,1234)
# print(s.name,s.Company,s.salary,s.pin)
# a = programmers("Asad",120000,1234)
# print(a.name,a.Company,a.salary,a.pin)

class programmer:
    def __init__(self,company,name,age,salary):
        self.company = company
        self.name = name
        self.age = age
        self.salary = salary

p = programmer("Microsoft","Ali",22,120000)
print(p.company,p.name,p.age,p.salary)
p = programmer("Microsoft","Mustafa",23,120000)
print(p.company,p.name,p.age,p.salary)
p = programmer("Microsoft","Owais",25,130000)
print(p.company,p.name,p.age,p.salary)