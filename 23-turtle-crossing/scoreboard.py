from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard (Turtle):
    
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)  # Near top center
        self.update_scoreboard()

    def update_scoreboard(self):
        """Clear and rewrite the current level and instructions."""
        self.clear()
        self.goto(0, 260)  # Ensure we write at the top each time
        self.write(
            f"Level: {self.level}  -  Use ↑ to move",
            align="center",
            font=FONT
        )

    def increase_level(self):
        """Increase level by 1 and refresh the display."""
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        """Display game over message and restart instructions."""
        self.clear()
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
        self.goto(0, -40)
        self.write("Press 'space' to play again", align="center", font=FONT)
