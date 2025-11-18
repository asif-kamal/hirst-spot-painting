###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import colorgram
import random
import turtle as t
from turtle import Screen

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    rgb_tuple = (color.rgb.r, color.rgb.g, color.rgb.b)
    rgb_colors.append(rgb_tuple)

rgb_colors =  rgb_colors[5:]
# print(rgb_colors)
t.colormode(255)
screen = Screen()

for _ in range(11):
    for _ in range(10):
        t.setheading(180)
        t.dot(15, random.choice(rgb_colors))
        t.penup()
        t.forward(25)
    t.penup()
    t.backward(250)
    t.setheading(90)
    t.forward(25)

screen.exitonclick()