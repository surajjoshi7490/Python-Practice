'''
volume of clyinder:- π r² h
surface area of clyinder :- 2πrh+2πr2'''
import math
class Cylinder:
    def __init__(self,height=1,radius=1):
        self.height=height
        self.radius=radius
    
    def volume (self):
        return f"The volume is {math.pi * (self.radius**2)*self.height}"
    
    def surface_area(self):
        a=2*(math.pi)*(self.radius)*(self.height)
        b=2*(math.pi)*(self.radius**2)
        return a+b 
    
    def __str__(self):
        return  f"This is the volume :- {self.volume()}\nThis is the Surface Area :- {self.surface_area()}"
    

data=Cylinder(2,3)
print(data)