from turtle import Turtle, _Screen

ALIGNMENT = "right"
FONT_SIZE = 12
FONT = ("courier", FONT_SIZE, "bold")


class Scoreboard(Turtle):

    def __init__(self, game_screen: _Screen):
        super().__init__(visible=False)
        self.up()
        self.level = 1
        self.screen_width = game_screen.window_width()
        self.screen_height = game_screen.window_height()
        self.print_level()

    def print_level(self):
        level_str = f"Level {self.level}"
        x_pos = -(self.screen_width / 2) + (FONT_SIZE * len(level_str))
        y_pos = (self.screen_height / 2) - (20 + FONT_SIZE)
        self.goto(x_pos, y_pos)
        self.write(level_str, align=ALIGNMENT, font=FONT)

    def next_level(self):
        self.level += 1
        self.clear()
        self.print_level()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
