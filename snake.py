from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake_bit = []
        self.create_snake()
        self.head = self.snake_bit[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_bit(position)

    def add_bit(self, position):
        new_snake = Turtle("square")
        new_snake.color("azure")
        new_snake.penup()
        new_snake.goto(position)
        self.snake_bit.append(new_snake)

    def extent(self):
        # adds a new segment to the snake
        self.add_bit(self.snake_bit[-1].position())

    def move(self):
        for seg_num in range(len(self.snake_bit) - 1, 0, -1):
            new_x = self.snake_bit[seg_num - 1].xcor()
            new_y = self.snake_bit[seg_num - 1].ycor()
            self.snake_bit[seg_num].goto(new_x, new_y)
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
