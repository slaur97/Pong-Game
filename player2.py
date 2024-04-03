from turtle import Turtle
coordonate=(370,0)

class Player2(Turtle):
    def __init__(self):
        super().__init__()
        self.create_player()
    def create_player(self):
        self.player=Turtle("square")
        self.player.penup()       
        self.player.color("white") 
        self.player.shapesize(stretch_wid=3,stretch_len=1)
        self.player.goto(x=coordonate[0],y=coordonate[1])
    def up(self):
        if(self.player.ycor() < 260):
            self.new_y=self.player.ycor()+30
            self.new_x=self.player.xcor()
            self.player.goto(self.new_x,self.new_y)
    def down(self):
        if(self.player.ycor() > -260):
            self.new_y=self.player.ycor()-30
            self.new_x=self.player.xcor()
            self.player.goto(self.new_x,self.new_y)
