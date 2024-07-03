from turtle import Turtle, _Screen
import os

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
FILE_PATH = "13_snake_game/high_score.txt"


class Scoreboard(Turtle):

    def __init__(self, screen: _Screen):
        super().__init__(visible=False)
        self.color("white")
        self.up()
        self.score = 0
        # Sets high score and loads it if available.
        self.high_score = 0
        if os.path.exists(FILE_PATH):
            with open(FILE_PATH) as file:
                self.high_score = int(file.read())
        # Prepares score printing
        self.screen_height = round(screen.window_height()/2) - 40
        self.print_score()

    def print_score(self):
        self.clear()
        score_str = f"Score: {self.score} | High score: {self.high_score}"
        self.write(score_str, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def add_point(self):
        self.score += 1
        self.print_score()

    def set_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(FILE_PATH, mode="w") as file:
                hs_str = str(self.high_score)
                file.write(hs_str)
        self.print_score()

    def restart(self):
        self.score = 0
        initial_pos = (0, self.screen_height)
        self.goto(initial_pos)
        self.print_score()
