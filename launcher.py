#!/usr/bin/python3
import os
import curses as crs

import model.plots as pl
import model.board as brd

import controller.settingloader as sl
import controller.keycontrols as kc
import controller.viewcontrols as vc

import view.boardview.tiledraw as td
__author__ = 'Kellan Childers'


def app(stdscr):
    vc.create_color_schemes()
    vc.init(stdscr)
    vc.setup.draw_background(stdscr)
    # vc.setup.do_commands(stdscr, kc.execute_command)

    # Show intro screen and start game.
    running = True
    for i in range(2):
        if i == 0:
            # Add all tiles to demo appearance.
            commands = [brd.clear_board, brd.demo]
            tile_count = 0
        else:
            # Clear screen and start game.
            commands = [brd.clear_board]
            tile_count = 2

        key = td.take_turn(stdscr, brd.board, *commands, tile_count=tile_count)
        try:
            running = kc.execute_command(key)
        except KeyError:
            pass

        if not running:
            break

    # Take turns continually until the game ends or player quits
    while running:
        key = td.take_turn(stdscr, brd.board, tile_count=0)
        try:
            running = kc.execute_command(key)
        except KeyError:
            pass

if __name__ == "__main__":
    os.chdir(sl.get_main_directory())

    crs.wrapper(app)
