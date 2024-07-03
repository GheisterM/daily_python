from turtle import Turtle, _Screen

ALIGNMENT = "center"
FONT_SIZE = 12
SCORE_FONT = ("courier", FONT_SIZE, "bold")
STATE_FONT = ("courier", 8, "bold")


class Scoreboard():

    def __init__(self, game_screen: _Screen) -> None:
        self.score_printer = self.make_printer()
        self.state_printer = self.make_printer()
        self.x_pos = 0
        self.y_pos = (game_screen.window_height()/2) - (20 + FONT_SIZE)
        self.score = 0
        self.print_score()

    def make_printer(self):
        new_printer = Turtle(visible=False)
        new_printer.up()
        return new_printer

    def print_score(self):
        self.score_printer.clear()
        score_str = f"Score: {self.score}"
        self.score_printer.goto(self.x_pos, self.y_pos)
        self.score_printer.write(score_str, align=ALIGNMENT, font=SCORE_FONT)

    def print_state(self, state_x, state_y, state_name):
        self.state_printer.goto(state_x, state_y)
        self.state_printer.write(state_name, align=ALIGNMENT, font=STATE_FONT)

    def game_over(self):
        self.score_printer.goto(self.x_pos, self.y_pos - 10 - FONT_SIZE)
        self.score_printer.write("GAME OVER", align=ALIGNMENT, font=SCORE_FONT)

    def add_point(self):
        self.score += 1
        self.print_score()
