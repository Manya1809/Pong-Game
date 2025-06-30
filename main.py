from turtle import Turtle , Screen 
from padle import Paddle
from BALL import Ball
from score import Scoreboard
import time
screen = Screen()
screen.setup(width= 800 ,height= 600)
screen.bgcolor("Black")
screen.title("pong")
screen.tracer(0)


r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up" , fun = r_paddle.go_up)
screen.onkey(key="Down" ,  fun = r_paddle.go_down)
screen.onkey(key="w" , fun = l_paddle.l_go_up)
screen.onkey(key="s" ,  fun = l_paddle.l_go_down)


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed )
    screen.update()
    ball.move_ball()

#collison detetction with wall
    if ball.ycor() > 280 or ball.ycor() < -280 :
        ball.bounce_y()
#collison detection with right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 : 
        ball.bounce_x()
        #scoreboard.r_score += 1
#collison detection with left paddle
    if ball.distance(l_paddle)< 50 and ball.xcor()< -320 :
        ball.bounce_x()
        #scoreboard.l_score += 1
#collison with right corner or Right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
#collison with left corner or left paddle misses
    if ball.xcor() < -380 :
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()