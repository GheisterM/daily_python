from turtle import Turtle, _Screen


class Snake:

    def __init__(self) -> None:
        self.score = 0
        self.body = []
        self.setup_snake()
        self.head = self.body[0]

    def setup_snake(self):
        for _ in range(3):
            self.grow()

    def grow(self):
        pos_index = len(self.body) - 1
        new_segment = Turtle(shape="square", visible=False)
        new_segment.color("white")
        new_segment.up()
        new_segment.speed(1)
        new_segment.backward(20*pos_index)
        self.body.append(new_segment)

    def border_collision(self, screen: _Screen):
        """Checks if the snake has hit or gone beyond screen borders"""

        return (abs(self.head.xcor()) >= (screen.window_width()/2)
                or abs(self.head.ycor()) >= (screen.window_height()/2))

    def body_collision(self):
        """Check if snake has hit (Or bit) it's own body"""
        for part in self.body[1:]:
            has_hit = self.head.pos() == part.pos()
            if has_hit:
                return True

        return False

    def forward(self, screen: _Screen):
        game_over = False
        for i in range(len(self.body)-1, 0, -1):
            new_pos = self.body[i-1].pos()
            self.body[i].goto(new_pos)
            if not self.body[i].isvisible():
                self.body[i].showturtle()

        self.head.forward(20)
        game_over = (
            self.border_collision(screen)
            or self.body_collision()
        )
        return game_over

    def turn_left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def turn_right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def turn_up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def turn_down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
