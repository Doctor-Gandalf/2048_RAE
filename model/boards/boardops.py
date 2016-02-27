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


def move_up(stdbrd):
    x_move, y_move = 0, 1
    old = pl.copy(stdbrd)

    for y in range(4):
        for x in range(4):
            try:
                stdbrd[y][x] += old[y + y_move][x + x_move]
                stdbrd[y + y_move][x + x_move] = None
                old[y + y_move][x + x_move] = None
            except TypeError:
                pass
            except IndexError:
                pass
            except ValueError:
                pass

    for y in range(1, 4):
        for x in range(4):
            i = y
            try:
                while stdbrd[i-1][x] is None:
                    stdbrd[i-1][x] = stdbrd[y][x]
                    stdbrd[i][x] = None
                    i -= 1
            except IndexError:
                pass

    place_tile(stdbrd)


def move_down(stdbrd):
    x_move, y_move = 0, 1
    old = pl.copy(stdbrd)

    for y in range(4, -1, -1):
        for x in range(4, -1, -1):
            try:
                stdbrd[y][x] += old[y - y_move][x - x_move]
                stdbrd[y - y_move][x - x_move] = None
                old[y - y_move][x - x_move] = None
            except TypeError:
                pass
            except IndexError:
                pass
            except ValueError:
                pass

    for y in range(3, -1, -1):
        for x in range(4, -1, -1):
            i = y
            try:
                while stdbrd[i+1][x] is None:
                    stdbrd[i+1][x] = stdbrd[y][x]
                    stdbrd[i][x] = None
                    i += 1
            except IndexError:
                pass

    place_tile(stdbrd)


def move_left(stdbrd):
    x_move, y_move = 1, 0
    old = pl.copy(stdbrd)

    for x in range(4):
        for y in range(4):
            try:
                stdbrd[y][x] += old[y][x + x_move]
                stdbrd[y][x + x_move] = None
                old[y][x + x_move] = None
            except TypeError:
                pass
            except IndexError:
                pass
            except ValueError:
                pass

    for x in range(1, 4):
        for y in range(4):
            i = x
            try:
                while stdbrd[y][i-1] is None:
                    stdbrd[y][i-1] = stdbrd[y][x]
                    stdbrd[y][i] = None
                    i -= 1
            except IndexError:
                pass

    place_tile(stdbrd)


def move_right(stdbrd):
    x_move, y_move = 1, 0
    old = pl.copy(stdbrd)

    for x in range(4, -1, -1):
        for y in range(4, -1, -1):
            try:
                stdbrd[y][x] += old[y][x - x_move]
                stdbrd[y][x - x_move] = None
                old[y][x - x_move] = None
            except TypeError:
                pass
            except IndexError:
                pass
            except ValueError:
                pass

    for x in range(3, -1, -1):
        for y in range(4, -1, -1):
            i = x
            try:
                while stdbrd[y][i+1] is None:
                    stdbrd[y][i+1] = stdbrd[y][x]
                    stdbrd[y][i] = None
                    i += 1
            except IndexError:
                pass

    place_tile(stdbrd)
