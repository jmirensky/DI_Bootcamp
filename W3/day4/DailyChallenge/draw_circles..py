
from DailyChallengeW3D4_Circle import circles
import turtle

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