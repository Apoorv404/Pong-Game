from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")

r_paddle = Paddle(x_pos=350, y_pos=0)
l_paddle = Paddle(x_pos=-350, y_pos=0)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=r_paddle.go_up, key="Up")
screen.onkey(fun=r_paddle.go_down, key="Down")
screen.onkey(fun=l_paddle.go_up, key="w")
screen.onkey(fun=l_paddle.go_down, key="s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with upper wall
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect right paddle miss
    if ball.xcor() > 360:
        ball.reset_position()
        scoreboard.l_point()

    # Detect left paddle miss
    if ball.xcor() < -360:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
