from .keyfunctions import *
__author__ = 'Kellan Childers'
"""Compile all user-facing functions here with easy to remember names to allow keymapping.
   Actual functions should be defined in controller.keycontrols.keyfunctions."""

functions = {
    "quit": finish,
    "continue": skip,
    "up": move_up,
    "down": move_down,
    "left": move_left,
    "right": move_right
}