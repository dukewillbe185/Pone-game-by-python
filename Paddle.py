from turtle import Turtle
class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.color('white')
        #self.setposition(350,0)
        self.shapesize(5, 1)
        self.penup()
        self.goto(position)
        # turtle.goto(20,20)

    def go_up(self):
        new_y =self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y =self.ycor() - 20
        self.goto(self.xcor(), new_y)


