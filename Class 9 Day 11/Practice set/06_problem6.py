# write str method to print the vector as follows:
"""7i + 8j + 10k"""

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
        return f"{self.x}i + {self.y}j + {self.z}k"
v1 = vector(1,2,3)
v2 = vector(4,5,6)
v3 = vector(7,8,9)
print(v1+v2+v3)
