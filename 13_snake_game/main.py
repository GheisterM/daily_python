from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from time import sleep

screen = Screen()
screen.title("Snake Game")
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

player = Snake()
food = Food(screen)
score = Scoreboard(screen)
screen.update()
screen.listen()
screen.onkey(fun=player.turn_left, key="Left")
screen.onkey(fun=player.turn_right, key="Right")
screen.onkey(fun=player.turn_up, key="Up")
screen.onkey(fun=player.turn_down, key="Down")

game_over = False
while not game_over:
    sleep(0.1)
    game_over = player.forward(screen)
    screen.update()
    if player.head.distance(food) < 15:
        food.reposition()
        score.add_point()
        player.grow()

score.game_over()

screen.exitonclick()
