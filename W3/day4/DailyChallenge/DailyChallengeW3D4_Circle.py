#Daily Challenge - Circle
#goal = create a class that represents a simple circle.

import math
import turtle

class Circle:

    '''Initialize the circle with a radius'''

    def __init__ (self, radius):
        self.radius = radius
       
    # Diameter as a property (calculated from radius)
    @property
    def diameter(self):
        return self.radius * 2
    
    # Optional setter:
    # Allows updating the radius automatically when the diameter is changed
    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2
    
    # Compute area of the circle (pi * radius squared)
    def area(self):
        return f"{math.pi * self.radius ** 2:,.2f}"

    #  Print the attributes of the circle - String representation
    def __str__(self):
        return f'Circle (radius = {self.radius})'
    
    #Add two circles together and return a new circle with the combined radius
    def __add__(self, other):
        if isinstance(other, Circle):
            return Circle(self.radius + other.radius)
        return NotImplemented       # addition with a non-Circle type is not supported
             
    #Compare two circles#  Greater than 
    def __gt__(self, other):
        return self.radius > other.radius
    
    # Check if two circles are equal
    def __eq__(self, other):
        return self.radius == other.radius
    
    # Less than (used for sorting circles)
    def __lt__(self, other):
        return self.radius < other.radius
    
c1 = Circle(7)

print(c1.diameter)  #14

c1.diameter = 20   
print(c1.radius)   # Change radius to 10

print(c1.area())   # 314.16

print(c1)   #Circle (radius = 10)

c2 = Circle(3)

c3 = c1 + c2
print(c3)  #Circle (radius = 13.0)

print(c1 > c2)     # True
print(c1 == c2)    # False
print(c1 < c2)     # False

c4 = Circle(20)
c5 = Circle(40)

# sorting
circles = [c1, c2, c3, c4, c5]
circles.sort()
for c in circles:
    print(c)

    # Circle (radius = 3)
    # Circle (radius = 10.0)
    # Circle (radius = 13.0)
    # Circle (radius = 20)
    # Circle (radius = 40)


# Bonus Challenge  
#Draw Circles

screen = turtle.Screen()
screen.title("Sorted Circles")

pen = turtle.Turtle()
pen.speed(0)
pen.width(2)

x_position = -150  # start drawing from the left

for circle in circles:
    pen.penup()
    pen.goto(x_position, 0)
    pen.pendown()
    pen.circle(circle.radius)

    x_position += circle.radius * 2 + 20  # space between circles

screen.mainloop()