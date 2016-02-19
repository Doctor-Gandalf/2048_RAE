#!/usr/bin/python3
import os
import controller.settingloader as sl
import model.plots as pl

__author__ = 'Kellan Childers'

if __name__ == "__main__":
    os.chdir(sl.get_main_directory())
    board = pl.Plot(4, 4)
    value = 2
    for x, y in pl.point_iterator(len(board), len(board[0])):
        board[x, y] = pl.Tile(value)
        value *= 2
        if value > 4096:
            value = 2
    print(board)
