from turtle import Turtle, Screen

donatello = Turtle()
screen = Screen()


def move_forward():
    donatello.forward(10)


def move_backwards():
    donatello.backward(10)


def turn_left():
    donatello.left(10)


def turn_right():
    donatello.right(10)


screen.listen()

screen.onkey(fun=move_forward, key="w")
screen.onkey(fun=move_backwards, key="s")
screen.onkey(fun=turn_left, key="a")
screen.onkey(fun=turn_right, key="d")
screen.onkey(fun=donatello.reset, key="c")

screen.exitonclick()
