import pandas
from turtle import Screen
from scoreboard import Scoreboard

IMAGE_PATH = "17_US_states_game/blank_states_img.gif"
IMAGE_WIDTH = 725
IMAGE_HEIGHT = 491

DATA_PATH = "17_US_states_game/50_states.csv"
MISSED_PATH = "17_US_states_game/missed_states.csv"

PROMPT_TITLE = "{}/50 states guessed"
PROMPT_TEXT = "Enter the name of a state:"

screen = Screen()
screen.setup(width=IMAGE_WIDTH, height=IMAGE_HEIGHT)
screen.bgpic(IMAGE_PATH)
screen.title("U.S. States Game")
screen.tracer(0)

score = Scoreboard(screen)

data = pandas.read_csv(DATA_PATH)
end_number = len(data)

keep_playing = True
while keep_playing and score.score < end_number:
    screen.update()
    guess = screen.textinput(
        title=PROMPT_TITLE.format(score.score),
        prompt=PROMPT_TEXT
    )

    if guess:
        guess = guess.title()
        result = data[data.state == guess]
        if not result.empty:
            score.add_point()
            score.print_state(
                int(result.iloc[0].x),
                int(result.iloc[0].y),
                guess
            )
            data = data[data.state != guess.title()]
    else:
        keep_playing = False

missed_states = data.state
missed_states.to_csv(MISSED_PATH)
score.game_over()
screen.update()

screen.exitonclick()
