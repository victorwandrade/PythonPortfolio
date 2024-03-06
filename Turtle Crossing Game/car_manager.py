from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10



class CarManager(Turtle):
    
    current_speed =  STARTING_MOVE_DISTANCE
    
    def __init__(self):
        super().__init__()
        STARTING_X = 360
        STARTING_Y = random.choice(range(-250, 250, 20))
        self.color(random.choice(COLORS))
        self.shape("square")
        self.shapesize(stretch_len = 2)
        self.penup()
        self.setheading(180)
        self.teleport(STARTING_X, STARTING_Y)
        #self.move()
        
    def move(self):
        self.forward(self.current_speed)
        

