import turtle
import time
import snake
screen = turtle.Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
turtle_body = [0, -20, -40]
screen.tracer(0)
snakey = snake.Snake()
screen.listen()
screen.onkey(snakey.up, "Up")
screen.onkey(snakey.down, "Down")
screen.onkey(snakey.left, "Left")
screen.onkey(snakey.right, "Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snakey.move_snake()
screen.exitonclick()
