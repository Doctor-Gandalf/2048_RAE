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


def move(stdbrd, direction):
    if direction == 'up':
        vertical_sum(stdbrd, (0, 1), pl.get_dimensions(stdbrd))
        vertical_slide(stdbrd, lambda x: x - 1, [[4], [1, 4]])
    elif direction == 'down':
        vertical_sum(stdbrd, (0, -1), [[4, -1, -1], [4, -1, -1]])
        vertical_slide(stdbrd, lambda x: x + 1, [[4, -1, -1], [3, -1, -1]])
    elif direction == 'left':
        horizontal_sum(stdbrd, (1, 0), pl.get_dimensions(stdbrd))
        horizontal_slide(stdbrd, lambda x: x - 1, [[4], [1, 4]])
    elif direction == 'right':
        horizontal_sum(stdbrd, (-1, 0), [[4, -1, -1], [4, -1, -1]])
        horizontal_slide(stdbrd, lambda x: x + 1, [[4, -1, -1], [3, -1, -1]])

        # place_tile(stdbrd)


def vertical_sum(stdbrd, move, dimensions):
    move_x, move_y = move
    width, height = dimensions
    old_board = pl.copy(stdbrd)

    for x, y in pl.points(width, height):
        try:
            stdbrd[x, y] += old_board[x + move_x, y + move_y]
            stdbrd[x + move_x, y + move_y] = None
            old_board[x + move_x, y + move_y] = None
        except TypeError:
            pass
        except IndexError:
            pass


def horizontal_sum(stdbrd, move, dimensions):
    move_x, move_y = move
    width, height = dimensions
    old_board = pl.copy(stdbrd)

    for y, x in pl.points(width, height):
        try:
            stdbrd[x, y] += old_board[x + move_x, y + move_y]
            stdbrd[x + move_x, y + move_y] = None
            old_board[x + move_x, y + move_y] = None
        except TypeError:
            pass
        except IndexError:
            pass


def vertical_slide(stdbrd, direction_function, dimensions):
    width, height = dimensions

    for x, y in pl.points(width, height):
        i = y
        try:
            while stdbrd[x, direction_function(i)] is None:
                stdbrd[x, direction_function(i)] = stdbrd[x, y]
                stdbrd[x, i] = None
                i = direction_function(i)
        except IndexError:
            pass


def horizontal_slide(stdbrd, direction_function, dimensions):
    width, height = dimensions

    for y, x in pl.points(width, height):
        i = x
        try:
            while stdbrd[direction_function(i), y] is None:
                stdbrd[direction_function(i), y] = stdbrd[x, y]
                stdbrd[i, y] = None
                i = direction_function(i)
        except IndexError:
            pass


def move_up(stdbrd):
    old_board = pl.copy(stdbrd)

    for x, y in pl.points_of(stdbrd):
        try:
            stdbrd[x, y] += old_board[x, y + 1]
            stdbrd[x, y + 1] = None
            old_board[x, y + 1] = None
        except TypeError:
            pass
        except IndexError:
            pass

    for x, y in pl.points([4], [1, 4]):
        i = y
        try:
            while stdbrd[x, i - 1] is None:
                stdbrd[x, i - 1] = stdbrd[x, y]
                stdbrd[x, i] = None
                i -= 1
        except IndexError:
            pass

            # place_tile(stdbrd)


def move_down(stdbrd):
    old_board = pl.copy(stdbrd)

    for x, y in pl.points([4, -1, -1], [4, -1, -1]):
        try:
            stdbrd[x, y] += old_board[x, y - 1]
            stdbrd[x, y - 1] = None
            old_board[x, y - 1] = None
        except TypeError:
            pass
        except IndexError:
            pass

    for x, y in pl.points([4, -1, -1], [3, -1, -1]):
        i = y
        try:
            while stdbrd[x, i + 1] is None:
                stdbrd[x, i + 1] = stdbrd[x, y]
                stdbrd[x, i] = None
                i += 1
        except IndexError:
            pass

            # place_tile(stdbrd)


def move_left(stdbrd):
    old_board = pl.copy(stdbrd)

    for y, x in pl.points_of(stdbrd):
        try:
            stdbrd[x, y] += old_board[x + 1, y]
            stdbrd[x + 1, y] = None
            old_board[x + 1, y] = None
        except TypeError:
            pass
        except IndexError:
            pass

    for y, x in pl.points([4], [1, 4]):
        i = x
        try:
            while stdbrd[i - 1, y] is None:
                stdbrd[i - 1, y] = stdbrd[x, y]
                stdbrd[i, y] = None
                i -= 1
        except IndexError:
            pass

            # place_tile(stdbrd)


def move_right(stdbrd):
    old_board = pl.copy(stdbrd)

    for y, x in pl.points([4, -1, -1], [4, -1, -1]):
        try:
            stdbrd[x, y] += old_board[x - 1, y]
            stdbrd[x - 1, y] = None
            old_board[x - 1, y] = None
        except TypeError:
            pass
        except IndexError:
            pass

    for y, x in pl.points([4, -1, -1], [3, -1, -1]):
        i = x
        try:
            while stdbrd[i + 1, y] is None:
                stdbrd[i + 1, y] = stdbrd[x, y]
                stdbrd[i, y] = None
                i += 1
        except IndexError:
            pass

            # place_tile(stdbrd)
