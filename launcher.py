#!/usr/bin/python3
from os import chdir
from curses import wrapper
from model.boards import board

import controller.settingloader as sl
import controller.viewcontrols as vc
import controller.gamecontrols as gc

__author__ = 'Kellan Childers'


def app(stdscr):
    # Initialize curses view.
    vc.create_color_schemes()
    vc.init(stdscr)

    # Start screen and run first command
    # should_play = gc.show_startup(stdscr, board)
    should_play = True

    if should_play:
        # Continue executing commands until app ends.
        gc.play_game(stdscr, board)


if __name__ == "__main__":
    # Set the cwd to the main directory to avoid load bugs.
    chdir(sl.get_main_directory())

    # Ensure app launches and exits without exceptions.
    wrapper(app)
