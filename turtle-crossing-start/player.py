from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    # TODO 1. Creating the Turtle player
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.go_to_start()

    # TODO 2. Moving the Turtle Forward
    def move_forward(self):
        self.forward(MOVE_DISTANCE)

    # If player reaches finish line

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

    # If player reaches finish line --> Next Level
    def go_to_start(self):
        self.goto(STARTING_POSITION)
