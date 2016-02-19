#!/usr/bin/python3
import os
import curses
import controller.settingloader as sl
import controller.viewcontrols as vc
import controller.keycontrols as kc
import model.boards as brd

__author__ = 'Kellan Childers'


def app(stdscr):
    vc.create_color_schemes()
    vc.init(stdscr)

    board = brd.board
    board = brd.demo(board)

    stdscr.addstr(0, 0, str(board))
    stdscr.refresh()

    key = stdscr.getkey()
    kc.do_commands(stdscr)

if __name__ == "__main__":
    # Set the cwd to the main directory to avoid load bugs.
    os.chdir(sl.get_main_directory())

    curses.wrapper(app)
