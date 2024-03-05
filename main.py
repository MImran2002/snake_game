import turtle
import time
import snake
import food
import scoreboard

screen = turtle.Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
turtle_body = [0, -20, -40]
screen.tracer(0)
snakey = snake.Snake()
food = food.Food()
scorey = scoreboard.Scoreboard()

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
    increment = 0
    if snakey.head.distance(food) < 15:
        food.refresh()
        scorey.change_score()
        snakey.extend()
    if snakey.head.xcor() > 280 or snakey.head.xcor() < -280 or snakey.head.ycor() > 280 or snakey.head.ycor() < -280:
        scorey.game_over()
        game_on = False
    for segment in snakey.segment:
        if segment == snakey.head:
            pass
        elif snakey.head.distance(segment) < 10:
            game_on = False
            scorey.game_over()


screen.exitonclick()
