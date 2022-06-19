from turtle import Screen
from turtle import Turtle
from Paddle import Paddle
from Ball import ball
import time
from Score import Score

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))

cossion = ball()


screen.listen()
screen.onkey(r_paddle.go_up,'Up')
screen.onkey(r_paddle.go_down,'Down')

screen.onkey(l_paddle.go_up,'w')
screen.onkey(l_paddle.go_down,'s')

game_is_on = True
score_board = Score()
while game_is_on:
    time.sleep(cossion.move_speed)
    screen.update()
    if cossion.ycor() == 300 or cossion.ycor() == -300:
        cossion.bounce_y()
    cossion.move()

    if cossion.distance(r_paddle) < 50 and cossion.xcor() > 320:
        cossion.bounce_x()

    if cossion.distance(l_paddle) < 50 and cossion.xcor() < -320:
        cossion.bounce_x()

    if cossion.xcor() > 380:
        cossion.ball_reset()
        score_board.get_lscore()

    if cossion.xcor() < -380:
        cossion.ball_reset()
        score_board.get_rscore()








screen.exitonclick()