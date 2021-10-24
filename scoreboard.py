from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("high_score.txt", mode="r") as file_high_score:
            self.high_score = int(file_high_score.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 275)
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score: {self.score}    High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", mode="w") as file_high_score:
                file_high_score.write(str(self.high_score))
        self.score = 0
        self.update()
