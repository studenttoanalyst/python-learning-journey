# create a class 'Employee' and add salary and increment properties to it.write a method 'salaryafterincrement' method with a 
# @property decorator with a setter which changes the value of increment based on the salary.

class Employee:
    Salary = 2000
    Increment = 20

    @property
    def salaryafterincrement(self,):
        return (self.Salary + self.Salary * (self.Increment/100))
    @salaryafterincrement.setter
    def salaryafterincrement(self,Salary):
        self.Increment = ((Salary/self.Salary)-1)*100
    
o = Employee()
print(o.salaryafterincrement)
o.salaryafterincrement = 2000
print(o.Increment)
print(o.salaryafterincrement)
















# class Employee:
#     salary = 234
#     increment = 20

#     @property
#     def salaryafterincrement(self):
#         return (self.salary + self.salary * (self.increment/100))
    
#     @salaryafterincrement.setter
#     def salaryafterincrement(self,salary):
#         self.increment= ((salary/self.salary)-1)*100
# o = Employee()
# print(o.salaryafterincrement)
# o.salaryafterincrement = 280
# print(o.increment)