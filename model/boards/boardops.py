import model.plots as pl
from .tile import Tile
__author__ = 'Kellan Childers'


def demo(stdbrd):
    board_copy = pl.copy(stdbrd)
    value = 2
    for x, y in pl.points(len(board_copy), len(board_copy[0])):
        board_copy[x, y] = Tile(value)
        value *= 2
        if value > 4096:
            value = 2
    return board_copy
