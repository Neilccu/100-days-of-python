import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle Crossing")

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

game_is_on = True

def restart_game():
    """Reset game state after GAME OVER."""
    global game_is_on, car_manager, player, scoreboard

    # Clear existing cars
    for car in car_manager.all_cars:
        car.hideturtle()
    car_manager.all_cars.clear()

    # Reset car speed (simplest: recreate CarManager)
    car_manager.__init__()  # reinitialize speed and list

    # Reset player position
    player.go_to_start()

    # Reset scoreboard
    scoreboard.level = 1
    scoreboard.update_scoreboard()

    # Turn game back on
    game_is_on = True

    # Rebind keys (in case)
    bind_keys()

    # Restart main loop
    run_game()


def bind_keys():
    screen.listen()
    screen.onkey(player.move_up, "Up")
    # Space (or Return) to restart after game over
    screen.onkey(restart_game, "space")


def run_game():
    global game_is_on

    while game_is_on:
        time.sleep(0.1)
        screen.update()

        # Create and move cars
        car_manager.create_car()
        car_manager.move_cars()

        # Detect collision with car
        for car in car_manager.all_cars:
            if car.distance(player) < 20:
                game_is_on = False
                scoreboard.game_over()

        # Detect successful crossing
        if player.is_at_finish_line():
            player.go_to_start()
            car_manager.level_up()
            scoreboard.increase_level()
            
bind_keys()
run_game()

screen.exitonclick()