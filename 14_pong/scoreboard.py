from turtle import Turtle, _Screen

ALIGNMENT = "center"
FONT = ("Courier", 60, "normal")


class Scoreboard(Turtle):

    def __init__(self, screen: _Screen):
        super().__init__(visible=False)
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.up()
        self.print_height = round(screen.window_height()/2) - 100
        self.print_width = 100
        self.print_score()

    def print_score(self):
        self.clear()
        self.goto(-self.print_width, self.print_height)
        self.write(self.l_score, align=ALIGNMENT, font=FONT)
        self.goto(self.print_width, self.print_height)
        self.write(self.r_score, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def add_point(self, side: int):
        if side == -1:
            self.l_score += 1
        else:
            self.r_score += 1
        self.print_score()
