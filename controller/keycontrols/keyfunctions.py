import model.boards as brd

__author__ = 'Kellan Childers'
"""Place functions which interact with the model here.
   Only functions defined here can be executed from a key command or mouse input."""


def skip(stdbrd):
    return True


def finish(stdbrd):
    return False


def board_up(stdbrd):
    brd.move(stdbrd, 'up')
    return True


def board_down(stdbrd):
    brd.move(stdbrd, 'down')
    return True


def board_left(stdbrd):
    brd.move(stdbrd, 'left')
    return True


def board_right(stdbrd):
    brd.move(stdbrd, 'right')
    return True
