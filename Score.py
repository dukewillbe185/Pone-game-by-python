from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.lscore = 0
        self.rscore = 0
        self.penup()
        self.hideturtle()
        self.update_board()

    def update_board(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.lscore, align='center', font=('Courier', 80, 'normal'))
        self.goto(100, 200)
        self.write(self.rscore, align='center', font=('Courier', 80, 'normal'))

    def get_rscore(self):
        self.rscore += 1
        self.update_board()

    def get_lscore(self):
        self.lscore += 1
        self.update_board()







