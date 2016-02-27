import model.boards as brd

__author__ = 'Kellan Childers'
"""Place functions which interact with the model here.
   Only functions defined here can be executed from a key command or mouse input."""


def skip(stdbrd):
    return True


def finish(stdbrd):
    return False


def board_up(stdbrd):
    brd.move_up(stdbrd)
    return True


def board_down(stdbrd):
    brd.move_down(stdbrd)
    return True


def board_left(stdbrd):
    brd.move_left(stdbrd)
    return True


def board_right(stdbrd):
    brd.move_right(stdbrd)
    return True
