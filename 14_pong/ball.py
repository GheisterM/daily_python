from turtle import Turtle, _Screen
import random

MIN_SPEED = 20
MAX_SPEED = 25
SPEED_UP_CONSTANT = 0.025


def random_speed():
    """Function to retrieve a random speed number."""

    return random.randint(MIN_SPEED, MAX_SPEED)/100


class Ball(Turtle):

    def __init__(self, game_screen: _Screen) -> None:
        super().__init__(shape="circle")
        self.color("white")
        self.up()
        self.screen_size = (
            game_screen.window_width(),
            game_screen.window_height()
        )
        self.x_speed = 0
        self.y_speed = 0
        self.spawn()

    def spawn(self):
        """Spawns the ball at the center, with a random speed
        that also sets direction.
        If it's a spawn after a score, faces opposite x direction."""

        self.goto(0, 0)
        x_direction = random.choice([-1, 1])
        if self.x_speed < 0:
            x_direction = 1
        elif self.x_speed > 0:
            x_direction = -1
        self.x_speed = random_speed() * x_direction
        self.y_speed = random_speed() * random.choice([-1, 1])

    def move(self, paddles: tuple[Turtle]):
        """Move and bounce function.
        If a paddle is missed, returns the score index of opposite paddle
        (-1 is Left Paddle, 1 is Right Paddle)"""

        if abs(self.ycor()) >= (self.screen_size[1]/2)-20:
            self.y_speed *= -1

        if abs(self.xcor()) > (self.screen_size[0]/2)-40:
            for paddle in paddles:
                if self.distance(paddle) < 50:
                    if ((self.x_speed < 0 and paddle.xcor() < 0) or
                            (self.x_speed > 0 and paddle.xcor() > 0)):
                        self.x_speed *= -1
                        self.speed_up()
                elif abs(self.xcor()) > self.screen_size[0]/2:
                    return -1 if self.xcor() > 0 else 1

        new_x = self.xcor() + self.x_speed
        new_y = self.ycor() + self.y_speed
        self.goto(new_x, new_y)
        return 0

    def speed_up(self):
        """Speed up function."""

        self.x_speed += SPEED_UP_CONSTANT
        self.y_speed += SPEED_UP_CONSTANT
