from gameboard import GameBoard
import time


is_game_on = True
game_board = GameBoard()

#Detect collision with food


def __checkSnakeFoodCollision(snake, food):
    if snake.head.distance(food) < 20:
        food.refresh_food()
        snake.eat_food()
        game_board.board_screen.update()


while is_game_on:
    game_board.board_snake.move_forward()
    time.sleep(0.1)
    game_board.board_screen.update()
    #if colide, the update the food, increment the snake length
    __checkSnakeFoodCollision(game_board.board_snake, game_board.board_food)



game_board.board_screen.exitonclick()