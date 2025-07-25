# write a class vector representing a vector of n dimensions overload the + and * operator which calculates the sum and dot products.

class vector:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def __add__(self,others):
        result = vector(self.x + others.x,self.y + others.y,self.z + others.z)
        return result
    def __mul__(self,others):
        result = vector(self.x*others.x,self.y*others.y,self.z*others.z)
        return result
    def __str__(self):
        return f"Vector{self.x}, {self.y}, {self.z}"
v1 = vector(1,2,3)
v2 = vector(4,5,6)
v3 = vector(7,8,9)
print(v1+v2+v3)
print(v1*v2*v3)