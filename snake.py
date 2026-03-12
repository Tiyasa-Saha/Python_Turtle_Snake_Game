from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    # Create the snake body
    def __init__(self):
        self.snake_list = []
        self.create_snake()
        self.head = self.snake_list[0]

    def create_snake(self):
        for i in range(0, 3):
            self.add_new_snake(0,0)

    def add_new_snake(self, x_axis, y_axis):
        new_snake = Turtle(shape="square")
        new_snake.color("White")
        new_snake.penup()
        new_snake.goto(x_axis, y_axis)
        self.snake_list.append(new_snake)
        x_axis -= 20

    def extend(self):
        self.add_new_snake(self.snake_list[-1].xcor(), self.snake_list[-1].ycor())

    # Get the snake to automatically move forward
    def move(self):
        for snake in range(len(self.snake_list) - 1, 0, -1):
            new_x = self.snake_list[snake - 1].xcor()
            new_y = self.snake_list[snake - 1].ycor()
            self.snake_list[snake].goto(new_x,new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)