from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("White")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.write_score()

    def update_score(self):
        self.clear()
        self.score += 1
        self.write_score()

    def write_score(self):
        self.write(f"Score: {self.score}", align="center", font=('Courier', 20, 'bold'))

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=('Courier', 20, 'bold'))
        self.goto(0, -30)
        self.write(f"Your score is: {self.score}", align="center", font=('Courier', 20, 'bold'))