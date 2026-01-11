from turtle import Turtle
import time

FONT = ("Courier", 30, "normal")
GOL_FONT = ("Courier", 50, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 250)
        self.write(self.l_score, align="center", font=FONT)
        self.goto(100, 250)
        self.write(self.r_score, align="center", font=FONT)

    def l_point(self):
        self.l_score += 1
        self.start_countdown()
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.start_countdown()
        self.update_scoreboard()

    def start_countdown(self):
        #self.clear(
        self.goto(0, 0)
        self.write("¡GOL!", align="center", font=GOL_FONT)
        self.getscreen().update()
        time.sleep(2)

        for count in range(3, 0, -1):
            self.clear()
            self.write(f"{count}", align="center", font=GOL_FONT)
            self.getscreen().update()
            time.sleep(1)
