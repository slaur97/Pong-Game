from turtle import Screen
from player1 import Player1
from player2 import Player2
from ball import Ball
from scorboard import Scorboard
import time

screen=Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


player1=Player1()
player2=Player2()
minge=Ball()
scoreboard=Scorboard()

screen.listen()
screen.onkey(player1.up,"Up")
screen.onkey(player1.down,"Down")
screen.onkey(player2.up,"w")
screen.onkey(player2.down,"s")



start=True
while start:
    time.sleep(0.05)
    screen.update()
    minge.ball_move()
    if minge.ball.ycor() > 300 or minge.ball.ycor() < -300:
        minge.new_pozition_y()
    if minge.ball.distance(player1.player) < 30  or minge.ball.distance(player2.player) < 30:
        minge.new_pozition_x()
    if minge.ball.xcor() > 400 or minge.ball.xcor() < -400:
        minge.reset_ball()
    if minge.ball.xcor()<-390:
        scoreboard.add_score_player1()
    if minge.ball.xcor()>390:
        scoreboard.add_score_player2()


screen.exitonclick()