from turtle import Turtle, Screen
import colorgram
import random


def teleport(t: Turtle, x: float, y: float):
    """Teleports the turtle to a given position without drawing."""
    t.up()
    t.setposition(x, y)
    t.down()


colorgram_colors = colorgram.extract('11_turtle_graphics/image.jpg', 40)
colors = []
for c_color in colorgram_colors:
    color_pattern = (c_color.rgb.r + c_color.rgb.g + c_color.rgb.b) / 3
    if color_pattern <= 240:
        colors.append(tuple(c_color.rgb))

donatello = Turtle()
donatello.hideturtle()
donatello.speed(10)
screen = Screen()
screen.colormode(255)

s_heigth = screen.window_height()
s_width = screen.window_height()

teleport(donatello, -(s_width/2), -(s_heigth/2) + 50)
while donatello.ycor() < (s_heigth/2) - 50:
    while donatello.xcor() < (s_width/2):
        donatello.dot(20, random.choice(colors))
        teleport(donatello, donatello.xcor() + 50, donatello.ycor())
    teleport(donatello, -(s_width/2), donatello.ycor() + 50)

screen.exitonclick()
