from gameboard import GameBoard
import time


is_game_on = True
game_board = GameBoard()

#Detect collision with food


def __check_snake_food_collision(snake, food):
    if snake.head.distance(food) < 20:
        food.refresh_food()
        snake.eat_food()
        game_board.board_screen.update()


def __check_snake_collide_with_itself(snake):
    return snake.collide_with_itself()


while is_game_on:
    game_board.board_snake.move_forward()
    time.sleep(0.1)
    game_board.board_screen.update()
    # if collide, the update the food, increment the snake length
    __check_snake_food_collision(game_board.board_snake, game_board.board_food)
    # if the snake collide with itself, declare game_over
    __check_snake_collide_with_itself(game_board.board_snake)



game_board.board_screen.exitonclick()