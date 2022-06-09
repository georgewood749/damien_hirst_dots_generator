import random
import turtle
import turtle as t


def row_of_circles(dot_size):
    for _ in range(10):
        tim.forward(dot_size * 2)
        tim.dot(dot_size, random.choice(colour_list))


def hirst_function(dot_size):
    y = -(dot_size * 10)
    for n in range(10):
        tim.setpos(-(dot_size * 10), y)
        row_of_circles(dot_size)
        y += dot_size * 2


colour_list = [(1, 12, 31), (53, 25, 17), (218, 127, 106), (10, 104, 159), (242, 213, 68), (149, 83, 39), (215, 87, 63),
               (155, 6, 24), (165, 162, 31), (157, 62, 102), (10, 64, 33), (206, 74, 104), (11, 96, 57), (95, 6, 20),
               (174, 135, 163), (1, 61, 145), (7, 172, 216), (3, 213, 207), (159, 33, 24), (8, 140, 85),
               (145, 227, 217), (122, 193, 147), (220, 177, 216), (100, 218, 229), (117, 171, 192), (79, 135, 178)]

turtle.colormode(255)
tim = t.Turtle()
tim.hideturtle()
tim.right(0)
tim.penup()

hirst_function(10)

screen = t.Screen()
screen.exitonclick()

