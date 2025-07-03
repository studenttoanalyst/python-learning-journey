class Employee: #CLass
    
    Language = "Py" #Attributes hein ye class k
    salary = 1200000 #Attributes hein ye class k
    def __init__(self):
        print("I m creating a program") # dundar method which is automatically caLLed
        
    def getinfo(self):
        print(f"The language is {self.Language} and the salary is {self.salary}")
    @staticmethod
    def static():
        print("Good boy jani")
harry = Employee() #object
harry.name = "Harry"
print(harry.name,harry.Language,harry.salary)

Owais = Employee()
Owais.name = "Owais"
print(Owais.name,Owais.Language,Owais.salary)
Owais.getinfo()
Owais.static()