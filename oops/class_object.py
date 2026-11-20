class Rectangle:

    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth

    def area(self):
        return self.length*self.breadth

    def perimeter(self):
        return 2*(self.length+self.breadth)

rect1=Rectangle(10,10)
print(rect1.area())
print(rect1.perimeter())


#------------------------------------------------------------------------------------


class Rectangle:
    def __init__(self,length=1,breadth=1):
        self.length=length
        self.breadth=breadth

    def area(self):
        return self.length*self.breadth

    def perimeter(self):
        return 2*(self.length+self.breadth) 

rect1=Rectangle()
rect2=Rectangle(10)
rect3=Rectangle(10,20)