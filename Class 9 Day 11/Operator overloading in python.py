# OPERATOR OVERLOADING IN PYTHON
"""Operators in Python can be overloaded using dunder methods.
   These methods are called when a given operator is used on the objects.
   Operators overloaded in python by using the following methods:
   
   pi+p2 = p1._add_(p2)
   pi-p2 = p1._sub_(p2)
   pi*p2 = p1._mul_(p2)
   pi/p2 = p1._truediv_(p2)
   pi//p2 = p1._floordiv_(p2)
   """

class Number:
    def __init__(self,n):
        self.n = n
    
    def __mul__(self,num):
        return self.n * num.n    


n = Number(1)
m = Number(2)

print(m * n)