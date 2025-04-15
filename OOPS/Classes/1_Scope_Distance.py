'''
I created a class to represent a line between two points.
It calculates the slope and distance using basic geometry formulas.
class line
two points (x1,y1) and (x2,y2)

to find :- slope and diatance
slope = y2-y1/x2-x1

a=(x2-x1)**2
b=(y2-y1)**2
diatance=sqrt(a)+(b)
'''
import math
class Line:
    def __init__(self,coor1,coor2):
        self.coor1=coor1
        self.coor2=coor2
    def slope(self):
        return (self.coor2[1]-self.coor1[1])/(self.coor2[0]-self.coor1[0])
    
    def distance(self):
        a=(self.coor2[0]-self.coor1[0])**2
        b=(self.coor2[1]-self.coor1[1])**2
        return math.sqrt((a)+(b))
    def __str__(self):
        return f"this is the value of slope {self.slope()}\nthis is the value of Distance {self.distance()}"
    
coordinate1=(3,2) # x1,y1
coordinate2=(8,10) #x2,y2
li=Line(coordinate1,coordinate2)
print(li)