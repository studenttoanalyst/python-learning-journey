# Q Add a static method in problem 2 to greet a user
class calculator:
    def __init__(self,n):
        self.n = n
    @staticmethod
    def greek():
        print("hello")
    def square(self):
        print(f"the square of n is {self.n*self.n}")
    def cube(self):
        print(f"the cube of n is {self.n*self.n*self.n}")
    def square_root(self):
        print(f"the square root of n is {self.n**1/2}")

p = calculator(6)
p.greek()
p.square()
p.cube()
p.square_root()