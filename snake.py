from turtle import Turtle

SNAKE_MOVING_DISTANCE = 20
SQUARE_SIZE = 20
RIGHT = 0
LEFT = 180
UP = 90
DOWN = 270


class Snake:
    def __init__(self):
        self.snake_segment = list()
        self.__create_snake_body()
        self.head = self.snake_segment[0]
        self.head.color("blue")
        self.tail=self.snake_segment[2]

    def __create_snake_body(self):
        for offset in range(3):
            new_square = Turtle("square")
            new_square.penup()
            new_square.color("white")
            new_square.goto(x=-offset * SQUARE_SIZE, y=0)
            self.snake_segment.append(new_square)

    def move_forward(self):
        for dot_position in range(len(self.snake_segment) - 1, 0, -1):
            new_x = self.snake_segment[dot_position - 1].xcor()
            new_y = self.snake_segment[dot_position - 1].ycor()
            self.snake_segment[dot_position].goto(x=new_x, y=new_y)
        self.snake_segment[0].forward(SNAKE_MOVING_DISTANCE)

    def turn_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def turn_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def turn_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def turn_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def eat_food(self):
        new_square = Turtle("square")
        new_square.penup()
        new_square.color("white")
        new_square.goto(x=self.tail.xcor(), y=self.tail.ycor())
        self.snake_segment.append(new_square)
        self.tail = new_square

    def collide_with_itself(self):
        for part in self.snake_segment[1:]:
            if part.distance(self.head) < 10:
                print("collide")
                return True
        return False

    def collide_with_wall(self):
        if(self.head.)
















