# create a class (2D vector) and use it to create another class representing a 3D vector
class twodvector:
    def __init__(self,i,j):
        self.i=i
        self.j = j
    def show(self):
        print(f"The vector is {self.i}i + {self.j}j")

class threedvector(twodvector):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k = k

    def show(self):
        print(f"The vectors are {self.i}i + {self.j}j + {self.k}k")
        

a = twodvector(1,2)
b = threedvector(4,5,6)

a.show()
b.show()














# class twodvector:
#     def __init__(self,i,j):
#         self.i = i
#         self.j = j
    
#     def show(self):
#         print(f"The vector is {self.i}i and {self.j}j")

# class threedvector(twodvector):
#     def __init__(self,k,i,j):
#         super().__init__(i,j)

#         self.k = k
#     def show(self):
#         print(f"The vectoe is {self.i}i + {self.j}j + {self.k}k")

# a = twodvector(1,2)
# b = threedvector(1,2,3)
# a.show()
# b.show()

        