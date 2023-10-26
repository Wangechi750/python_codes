#creating a class and object
class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
       a=self.length*self.width
       return a
    def perimeter(self):
       p=2*(self.length+self.width)
       return p
rect=Rectangle(10,5)
print(rect.perimeter())
print(rect.area())