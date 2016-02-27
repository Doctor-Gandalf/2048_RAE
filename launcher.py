#!/usr/bin/python3
import os
import curses
import controller.settingloader as sl
import controller.viewcontrols as vc
import controller.gamecontrols as gc
from model.boards import board

__author__ = 'Kellan Childers'


def app(stdscr):
    # Initialize curses view.
    vc.create_color_schemes()
    vc.init(stdscr)

    # Start screen and run first command
    should_play = gc.show_startup(stdscr, board)

    if should_play:
        # Continue executing commands until app ends.
        gc.play_game(stdscr, board)


if __name__ == "__main__":
    # Set the cwd to the main directory to avoid load bugs.
    os.chdir(sl.get_main_directory())

    # Ensure app launches and exits without exceptions.
    curses.wrapper(app)
