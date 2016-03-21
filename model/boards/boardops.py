import model.plots as pl
import model.dice as dc
from .tile import Tile

__author__ = 'Kellan Childers'


def demo(stdbrd):
    """Show a demo screen for the board.

    :param stdbrd: the standard board
    :return: a demo version of the board.
    """
    board_copy = pl.copy(stdbrd)
    value = 2
    for x, y in pl.points(len(board_copy), len(board_copy[0])):
        board_copy[x, y] = Tile(value)
        value *= 2
        if value > 4096:
            value = 2
    return board_copy


def clear_board(stdbrd):
    """Clear the board.
    Note: Duplicates plot clear, to keep all board ops in one space.

    :param stdbrd: the board to clear
    :return: the cleared board
    """
    return pl.clear(stdbrd)


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


def move_tiles(stdbrd, direction):
    if direction == 'up':
        sum_tiles(stdbrd, move=(0, 1), dimensions=pl.get_dimensions(stdbrd))
        vertical_slide(stdbrd, dir_func=lambda x: x - 1, dimensions=[[4], [1, 4]])
    elif direction == 'down':
        sum_tiles(stdbrd, move=(0, -1), dimensions=[[4, -1, -1], [4, -1, -1]])
        vertical_slide(stdbrd, dir_func=lambda x: x + 1, dimensions=[[4, -1, -1], [3, -1, -1]])
    elif direction == 'left':
        sum_tiles(stdbrd, move=(1, 0), dimensions=pl.get_dimensions(stdbrd), horizontal=True)
        horizontal_slide(stdbrd, dir_func=lambda x: x - 1, dimensions=[[4], [1, 4]])
    elif direction == 'right':
        sum_tiles(stdbrd, move=(-1, 0), dimensions=[[4, -1, -1], [4, -1, -1]], horizontal=True)
        horizontal_slide(stdbrd, dir_func=lambda x: x + 1, dimensions=[[4, -1, -1], [3, -1, -1]])

    place_tile(stdbrd)


def sum_tiles(stdbrd, move, dimensions, horizontal=False):
    move_x, move_y = move
    width, height = dimensions
    old_board = pl.copy(stdbrd)

    for x, y in pl.points(width, height):
        if horizontal:
            x, y = (x, y)[::-1]
        try:
            stdbrd[x, y] += old_board[x + move_x, y + move_y]
            stdbrd[x + move_x, y + move_y] = None
            old_board[x + move_x, y + move_y] = None
        except TypeError:
            pass
        except IndexError:
            pass


def vertical_slide(stdbrd, dir_func, dimensions):
    width, height = dimensions

    for x, y in pl.points(width, height):
        i = y
        try:
            while stdbrd[x, dir_func(i)] is None:
                stdbrd[x, dir_func(i)], stdbrd[x, y] = stdbrd[x, y], stdbrd[x, dir_func(i)]
                i = dir_func(i)
        except IndexError:
            pass


def horizontal_slide(stdbrd, dir_func, dimensions):
    width, height = dimensions

    for y, x in pl.points(width, height):
        i = x
        try:
            while stdbrd[dir_func(i), y] is None:
                stdbrd[dir_func(i), y], stdbrd[x, y] = stdbrd[x, y], stdbrd[dir_func(i), y]
                i = dir_func(i)
        except IndexError:
            pass
