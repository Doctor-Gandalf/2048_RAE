import curses
__author__ = 'Kellan Childers'


def init(stdscr):
    """Start up standard screen to allow easy setup for apps.

    :param stdscr: the standard screen used in curses
    :return: null
    """
    # Ensures a clean visual space.
    stdscr.clear()
    curses.curs_set(False)

    # Set the background of the app to the secondary color.
    stdscr.bkgd(' ', curses.color_pair(1))
    stdscr.refresh()
