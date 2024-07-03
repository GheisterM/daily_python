from turtle import Turtle, _Screen


class Player(Turtle):

    def __init__(self, game_screen: _Screen):
        super().__init__(shape="turtle")
        self.color("green")
        self.up()
        self.setheading(90)
        self.screen_width = game_screen.window_width()
        self.screen_height = game_screen.window_height()
        self.respawn()

    def respawn(self):
        y_pos = -(self.screen_height/2) + 20
        self.goto(0, y_pos)

    def move(self):
        self.forward(10)
