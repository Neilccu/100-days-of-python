from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        """Randomly create a new car on the left side of the screen."""
        # 1 in 6 chance each loop
        if random.randint(1, 6) == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)  # rectangle
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(-300, random_y)  # left side, move to the right
            self.all_cars.append(new_car)

    def move_cars(self):
        """Move all cars to the right according to current speed."""
        for car in self.all_cars:
            car.forward(self.car_speed)

    def level_up(self):
        """Increase car speed for the next level."""
        self.car_speed += MOVE_INCREMENT
