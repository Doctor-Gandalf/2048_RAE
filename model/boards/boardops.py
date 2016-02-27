import model.plots as pl
import model.dice as dc
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


def place_tile(stdbrd):
    """Place a tile randomly on the board.

    :param stdbrd: the standard board
    :return: the board
    """
    tile = Tile(2) if dc.roll(1, 6) >= 2 else Tile(4)
    done = False
    if None not in stdbrd:
        raise IndexError("Could not place tile")
    while not done:
        x = dc.roll(1, 4) - 1
        y = dc.roll(1, 4) - 1
        if stdbrd[x][y] is None:
            stdbrd[x][y] = tile
            done = True
    return stdbrd
