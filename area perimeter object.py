#creating a class and object
class Circle:
    def __init__(self,radius):
        self.radius=radius
    def perimeter(self):
       p=2*3.14*self.radius
       return p
    def area(self):
       a=2*3.14*self.radius*self.radius
       return a
radius=Circle(5)
print(radius.perimeter())
print(radius.area())