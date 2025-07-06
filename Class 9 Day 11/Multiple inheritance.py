# MULTIPLE INHERITANCE
"""mULTIPLE INHERITANCE OCCURS WHEN THE CHILD CLASS INHERITS FROM MORE THAN ONE PARENT CLASSES"""
class Employee:
    company = "ITC"
    name = "owais"
    salary = 122
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")


class coder:
    language = "python"
    def printlanguages(self):
        print(f"Out of all the languages her is your language: {self.language}")
class Programmer(Employee,coder):
    company = "ITC infotech"
    def showlanguage(self):
        print(f"the name is {self.name} and the good with {self.language} language")

a = Employee()
b = Programmer()
b.show()
b.showlanguage()
b.printlanguages()
a.show()
 

