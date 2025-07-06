# create a class 'pets' from a class 'Animals' and further create a class 'Dog' from 'pets' Add a method 'bark' to class 'dog'

class Animals:
    pass
class Pets(Animals):
   pass
class Dog(Pets):
    def bark(self):
        print("Bow Bow!!!!")


a = Dog()
a.bark()


