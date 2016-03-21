import controller.keycontrols as kc
import model.boards as brd
__author__ = 'Kellan Childers'


def show_startup(stdscr, stdbrd):
    """Show the startup screen and run first command.

    :param stdscr: the standard screen
    :param stdbrd: the standard board
    :return: whether or not to continue the game
    """
    # Setup board.
    stdbrd = brd.demo(stdbrd)
    stdscr.addstr(0, 0, str(stdbrd))
    stdscr.refresh()

    key = stdscr.getkey()
    should_continue = True
    try:
        should_continue = kc.execute_command(key, stdbrd)
    except IndexError:
        # Index errors happen when player tries to move the screen, and should be ignored.
        pass
    except KeyError:
        # Key errors happen when players hit a key that isn't in the keymap, and should be ignored.
        pass

    return should_continue


def play_game(stdscr, stdbrd):
    """Execute commands repeatedly until told to stop.
    Note: Uses specific curses functionality.

    :param stdscr: the standard screen.
    :param stdbrd: the standard board
    :return: null
    """
    # Add two tiles at start of game.
    stdbrd = brd.place_tile(stdbrd)
    stdbrd = brd.place_tile(stdbrd)

    import model.plots as pl
    for x, y in pl.points_of(stdbrd):
        stdbrd[x, y] = 2

    running = True
    while running:
        # Show the board.
        stdscr.clear()
        stdscr.addstr(0, 0, str(stdbrd))
        stdscr.refresh()

        key = stdscr.getkey()
        try:
            running = kc.execute_command(key, stdbrd)
        except KeyError:
            running = True
