import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.up,"Up")

cars = []
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
           
    # Create a new car at a random time
    if random.randint(1, 6) == 1:  # Adjust probability as needed
        new_car = CarManager()
        cars.append(new_car)
        
    if player.ycor() > 280:
        scoreboard.increase_score()
        CarManager.current_speed += 10
        player.reset()

    # Move all existing cars
    for car in cars:
        car.move()

        # Remove cars that have gone off-screen
        if car.xcor() < -350:
            cars.remove(car)
            
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False

    
screen.exitonclick()