from turtle import Turtle

class Scorboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_player1=0
        self.score_player2=0
        self.color("white")
        self.penup()
        self.goto(x=0,y=250)
        self.write(f"{self.score_player1}   {self.score_player2}",align="center",font=("Arial", 24, "normal"))
        self.hideturtle()

    def add_score_player1(self):
        self.clear()
        self.score_player1+=1
        self.write(f"{self.score_player1}   {self.score_player2}",align="center",font=("Arial", 24, "normal"))
    def add_score_player2(self):
        self.clear()
        self.score_player2+=1
        self.write(f"{self.score_player1}   {self.score_player2}",align="center",font=("Arial", 24, "normal"))