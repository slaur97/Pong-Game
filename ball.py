from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.create_ball()
        self.xmove=-10
        self.ymove=-10

    def create_ball(self):
        self.ball=Turtle(shape="circle")
        self.ball.penup()
        self.ball.color("white")

    def ball_move(self):
        self.xcor=self.ball.xcor()+self.xmove
        self.ycor=self.ball.ycor()+self.ymove
        self.ball.goto(self.xcor,self.ycor)
    def new_pozition_y(self):
        self.ymove *=-1
    def new_pozition_x(self):
        self.xmove *=-1

    def reset_ball(self):
        self.ball.goto(0,0)
        self.new_pozition_x()