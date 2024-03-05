from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.increment = 0
        self.penup()
        self.goto(0, 230)
        self.pendown()
        self.color("white")
        self.write(f"Score : {self.increment}", align="center", font=("Arial", 25, "normal"))
        self.hideturtle()

    def change_score(self):
        self.clear()
        self.increment += 1
        self.write(f"Score : {self.increment}", align="center", font=("Arial", 25, "normal"))


    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align = "center", font=("Arial", 40, "bold"))