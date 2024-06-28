from turtle import Turtle, Screen
import random

finished = True
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []
screen = Screen()
screen.setup(width=500, height=400)

user_bet = ""
while user_bet not in colors:
    user_bet = screen.textinput(
        title="Make your bet",
        prompt="Which turtle will win the race? " + "/".join(colors)
    )

for index, color in enumerate(colors):
    turtles.append(Turtle(shape="turtle"))
    turtles[-1].color(color)
    turtles[-1].up()
    x_pos = -(screen.window_width()/2) + 20
    y_pos = -(screen.window_height()/4) + (30 * (index+1))
    turtles[-1].goto(x=x_pos, y=y_pos)

if user_bet in colors:
    finished = False

while not finished:
    for t in turtles:
        t.forward(random.randint(1, 10))
        if t.xcor() >= screen.window_width()/2:
            finished = True
            if t.pencolor() == user_bet:
                print(f"You win! {t.pencolor()} is the winner!")
            else:
                print(f"You lose! {t.pencolor()} is the winner!")
            break

screen.exitonclick()
