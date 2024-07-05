from turtle import Turtle, _Screen
from player import Player
import random

CAR_SIZE = 2
CAR_SPEED_UP = 0.05


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


class CarManager:

    def __init__(self, game_screen: _Screen):
        self.screen_width = game_screen.window_width()
        self.screen_height = game_screen.window_height()
        self.car_speed = 0.1
        self.cars = self.spawn()

    def spawn(self):
        """Spawns all car rows by calculating the amount
        of rows that fits within the screen."""

        row_y = -(self.screen_height / 2) + 60
        cars = self.random_row(row_y)  # Instantiates first row

        # Calculates row amount according to screen height
        # row_amount = (screen_height - minimum space) / separation
        # We use a separation of 20 pixels to make the screen less cluttered
        # Minimum space adjusted to my screen and general values.
        # You may adjust to your liking!
        row_amount = round((self.screen_height - 140) / 30)

        for i in range(row_amount):
            if i % 2 == 0:
                # Calculates y position according to player and first row
                row_y = -(self.screen_height / 2) + 120 + (30 * i)
                new_row = self.random_row(row_y)    # Spawns a new row
                cars.extend(new_row)   # Extends the list of cars

        return cars

    def random_row(self, y_pos: int):
        """Spawns all cars in a row, leaving a minimum separation
        of 20 pixels between them."""

        row_heading = random.choice((0, 180))

        max_cars = round(self.screen_width / 100) - 1
        total_cars = random.randint(1, max_cars)

        row = [Turtle(shape="square") for _ in range(total_cars)]

        last_x = -(self.screen_width/2)

        for car in row:
            car.shapesize(stretch_wid=1, stretch_len=CAR_SIZE)
            car.up()
            car.color(random_color())
            car.setheading(row_heading)
            x_pos = random.randint(last_x, last_x + (20 * CAR_SIZE * 3))
            car.goto(x_pos, y_pos)
            last_x = x_pos + (20 * CAR_SIZE) + 20

        return row

    def has_collided(self, player: Player, car: Turtle):
        """Check if the player has reached the y position of a car
        and if it has collided with it."""
        player_y = player.ycor()
        car_y = car.ycor()
        y_distance = abs(player_y - car_y)

        # Here we need to set the "safe y" according to turtle position
        # due to the turtle head being beyond 20 pixels.
        safe_y = 23 if car_y > player_y else 20

        if y_distance < safe_y and car.distance(player) < (10 * CAR_SIZE) + 5:
            return True

        return False

    def move(self, player: Player):
        """Moves the cars, and return if any of them has collided
        with the turtle, thus triggering game over.

        Returns game over (True/False)"""

        for car in self.cars:
            car.forward(self.car_speed)
            if self.has_collided(player, car):
                return True

            if (car.heading() == 0 and
                    car.xcor() > (self.screen_width / 2) + 80):
                new_x = -(self.screen_width / 2) - 80
                car.goto(new_x, car.ycor())
            elif (car.heading() == 180 and
                    car.xcor() < -(self.screen_width / 2) - 80):
                new_x = (self.screen_width / 2) + 80
                car.goto(new_x, car.ycor())

        return False

    def respawn(self):
        for old_car in self.cars:
            old_car.goto(self.screen_width*2, self.screen_height*2)

        self.cars.clear()

        self.cars = self.spawn()

    def speed_up(self):
        self.car_speed += CAR_SPEED_UP
