from turtle import Turtle, _Screen

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self, screen: _Screen):
        super().__init__(visible=False)
        self.score = 0
        self.color("white")
        self.up()
        screen_height = round(screen.window_height()/2) - 40
        initial_pos = (0, screen_height)
        self.goto(initial_pos)
        self.print_score()

    def print_score(self):
        self.clear()
        score_str = f"Score: {self.score}"
        self.write(score_str, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def add_point(self):
        self.score += 1
        self.print_score()
