import random
import time
import turtle
from turtle import Turtle, Screen

screen = Screen()
tim = Turtle()
screen.tracer(0)


def move_forward():
    while tim.xcor() > -305:
        tim.forward(5)
        time.sleep(0.1)
        screen.update()


screen.setup(600, 600)
tim.shape("square")
tim.color("black")
tim.goto(290, 0)
tim.setheading(180)
move_forward()


turtle.done()
