from .keyfunctions import *
__author__ = 'Kellan Childers'
"""Compile all user-facing functions here with easy to remember names to allow keymapping.
   Actual functions should be defined in controller.keycontrols.keyfunctions."""

functions = {
    'skip': skip,
    'quit': finish,
    'up': board_up,
    'down': board_down,
    'left': board_left,
    'right': board_right
}