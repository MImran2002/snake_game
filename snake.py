import turtle

turtle_body = [0, -20, -40]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 360

class Snake:

    def __init__(self):
        self.segment = []
        self.create_snake()

    def create_snake(self):
        for a in range(3):
            turt = turtle.Turtle("square")
            turt.color("white")
            turt.penup()
            turt.goto(turtle_body[a], 0)
            self.segment.append(turt)

    def move_snake(self):
        for seg in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[seg - 1].xcor()
            new_y = self.segment[seg - 1].ycor()
            self.segment[seg].goto(new_x, new_y)
        self.segment[0].forward(20)

    def up(self):
        if self.segment[0].heading() != DOWN:
            self.segment[0].setheading(UP)

    def down(self):
        if self.segment[0].heading() != UP:
            self.segment[0].setheading(DOWN)

    def left(self):
        if self.segment[0].heading() != RIGHT:
            self.segment[0].setheading(LEFT)

    def right(self):
        if self.segment[0].heading() != LEFT:
            self.segment[0].setheading(RIGHT)
