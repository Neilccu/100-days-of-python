from turtle import Turtle, Screen
from random import Random

screen = Screen()
is_race_on = False
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? red, orange, yellow, green,"
                                                          " blue or purple? Pick one: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = {}
STARTING_X = -230
STARTING_Y = -90
SEPARATION = 30

for color in colors:
    tim = Turtle(shape="turtle")
    tim.color(color)
    tim.penup()
    turtles[color] = tim

    turtles[color].goto(STARTING_X, STARTING_Y)
    STARTING_Y += SEPARATION

if user_bet:
    is_race_on = True

while is_race_on:

    for key in turtles:
        rand_distance = Random.randint(0,10)
        turtles[key].forward(rand_distance)
        if turtles[key].xcor() >= 230:
            is_race_on = False
            winning_color = turtles[key].pencolor()
            if winning_color == user_bet:
                print(f"You've won! the {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
            break


screen.exitonclick()

