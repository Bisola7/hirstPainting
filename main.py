from turtle import Turtle, Screen
import turtle
import random
# import colorgram
# program to extract colors from an image into tuple (r, g, b)
# colors = colorgram.extract('image.jpg', 6)
# rgb_colors = []
# for c in colors:
#     r = c.rgb.r
#     g = c.rgb.g
#     b = c.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)
color_list = [(246, 245, 243), (233, 239, 246), (246, 239, 242), (240, 246, 243), (132, 166, 205), (221, 148, 106)]
turtle.colormode(255)
t = Turtle()
t.penup()
t.hideturtle()
t.speed("fastest")
t.setheading(225)
t.forward(300)
t.setheading(0)
no_of_dot = 100
for i in range(1, no_of_dot + 1):
    t.dot(20, random.choice(color_list))
    t.forward(50)
    if i % 10 == 0:
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)

s = Screen()
s.exitonclick()
