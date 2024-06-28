from turtle import Turtle, _Screen
import random


class Food(Turtle):

    def __init__(self, screen: _Screen):
        super().__init__("circle")
        self.up()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("red")
        self.speed(0)
        self.screen_width = round(screen.window_width()/2) - 20
        self.screen_height = round(screen.window_height()/2) - 20
        self.reposition()

    def reposition(self):
        random_x = random.randint(-self.screen_width, self.screen_width)
        random_y = random.randint(-self.screen_height, self.screen_height)
        self.goto(random_x, random_y)
