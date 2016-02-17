from model.board import move, board
__author__ = 'Kellan Childers'
"""Place functions which interact with the model here.
   Only functions defined here can be executed from a key command or mouse input."""


def finish():
    return False


def skip():
    return True


def move_up():
    move(board, (0, 1))


def move_down():
    move(board, (0, -1))


def move_left():
    move(board, (1, 0))


def move_right():
    move(board, (-1, 0))