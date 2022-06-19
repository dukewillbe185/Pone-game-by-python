from turtle import Turtle
import random

class ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.goto(0,0)
        self.penup()
        self.shapesize(1.5,1.5)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.8

    def ball_reset(self):
        self.move_speed = 0.1
        self.goto(0,0)
        self.bounce_x()






