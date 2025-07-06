# CLASS METHOD
"""A Class method is a method which is bound to the class and not the object of the class.
   @classmethod decorator is used to create a class method. """


class Employee:
    a = 1
    @classmethod
    def show(self):
        print(f"The value of a attribute is {self.a}")

o =Employee()
o.a =44
o.show()