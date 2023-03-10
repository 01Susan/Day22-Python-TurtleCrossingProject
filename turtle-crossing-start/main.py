import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
screen.tracer(0)
player = Player()
screen.listen()
screen.onkey(player.move_forward, "Up")
cars = CarManager()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_cars()
    cars.move_cars()

    for car in cars.all_cars:
        if player.distance(car) < 20:
            scoreboard.game_over()
            time.sleep(2)
            game_is_on = False
    if player.is_at_finish_line():
        scoreboard.increase_level()
        player.go_to_start()
        cars.level_up()
