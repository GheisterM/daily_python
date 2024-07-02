from turtle import Turtle, _Screen


class Paddle(Turtle):

    def __init__(self, game_screen: _Screen, screen_offset: int) -> None:
        super().__init__(shape="square")
        self.screen_height = game_screen.window_height()
        self.screen_width = game_screen.window_width()
        x_pos = ((self.screen_width * screen_offset)/2)-(20*screen_offset)
        self.color("white")
        self.up()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(x_pos, 0)

    def move_up(self):
        x_pos = self.xcor()
        y_pos = self.ycor() + 20
        target_pos = y_pos + (20 * round(self.shapesize()[0]/2))
        if target_pos < self.screen_height/2:
            self.goto(x_pos, y_pos)

    def move_down(self):
        x_pos = self.xcor()
        y_pos = self.ycor() - 20
        target_pos = y_pos - (20 * round(self.shapesize()[0]/2))
        if target_pos > -(self.screen_height/2):
            self.goto(x_pos, y_pos)
