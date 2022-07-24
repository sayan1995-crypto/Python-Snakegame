from turtle import Turtle, Screen
from snake import Snake
from food import Food


class GameBoard:

    @staticmethod
    def __board_setup():
        board_screen = Screen()
        board_snake = Snake()
        board_food = Food()
        board_screen.setup(width=600, height=600)
        board_screen.bgcolor("black")
        board_screen.title("My Snake Game")
        board_screen.tracer(0)
        board_screen.listen()
        board_screen.onkeypress(board_snake.turn_up, "Up")
        board_screen.onkeypress(board_snake.turn_down, "Down")
        board_screen.onkeypress(board_snake.turn_left, "Left")
        board_screen.onkeypress(board_snake.turn_right, "Right")
        return board_screen, board_snake, board_food

    def __init__(self):
        self.board_screen, self.board_snake, self.board_food = GameBoard.__board_setup()


if __name__== '__main__':
    g=GameBoard()
    print(g)



