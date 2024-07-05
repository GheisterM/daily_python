from turtle import Screen
# from time import sleep
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.colormode(255)
screen.title("Turtle Crossing")
screen.tracer(0)
player = Player(screen)
cars = CarManager(screen)
score = Scoreboard(screen)

screen.listen()
screen.onkey(fun=player.move, key="Up")

game_over = False

while not game_over:
    game_over = cars.move(player)
    if player.ycor() >= screen.window_height()/2:
        player.respawn()
        score.next_level()
        cars.respawn()
        cars.speed_up()
    screen.update()

score.game_over()

screen.exitonclick()
