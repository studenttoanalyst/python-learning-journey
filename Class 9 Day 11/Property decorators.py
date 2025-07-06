# @PROPERTY
"""method ko variable ki tarah use karna"""

# Problem: Tum method likhtay ho, par use variable ki tarah karna chahtay ho
"""Normally Python mein agar koi method ho """
# class student:
    
#     def name(self):
#         self.name = "Owais"
#         print(self.name)

# """Tum aise call karogay"""
# o = student()
# o.name()
"""Lekin agar tum chaho ke method ko variable ki tarah use karo (without ()), 
   to Python mein uske liye @property decorator hota hai.
"""

class Student:
    def __init__(self, name):
        self._name = name  # Use a private variable

    @property
    def name(self):
        return self._name  # Return the private variable  
o = Student("Ali")
print(o.name)

# Agar tum chaho ke naam change bhi ho sake (set kar sako)
"""Tab use karte hain: @x.setter"""

class Student:
    def __init__(self, name):
        self._name = name  # Use a private variable

    @property
    def name(self):
        return self._name  # Return the private variable  
    @name.setter
    def name(self,newname):
        if len(newname) < 3:
            print("Name chota h")
        else:
            self._name = newname
o = Student("Ali")
print(o.name)

o.name = "Owais"
print(o.name)

