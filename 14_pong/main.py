from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=900, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

l_paddle = Paddle(screen, -1)
r_paddle = Paddle(screen, 1)
ball = Ball(screen)
score = Scoreboard(screen)
screen.update()
screen.listen()
screen.onkey(fun=r_paddle.move_up, key="Up")
screen.onkey(fun=r_paddle.move_down, key="Down")
screen.onkey(fun=l_paddle.move_up, key="w")
screen.onkey(fun=l_paddle.move_down, key="s")

while True:
    point = ball.move((l_paddle, r_paddle))
    if point != 0:
        ball.spawn()
        score.add_point(point)
    screen.update()

screen.exitonclick()
