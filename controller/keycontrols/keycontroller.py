from ..settingloader import read_settings
from .functiondict import functions
__author__ = 'Kellan Childers'

main_keys = read_settings('keybindings.config')


def execute_command(key, key_set=main_keys):
    """Execute a key command based on a key binding.

    :param key: the key command to execute
    :param key_set: the set of keys execute based on (default main_keys)
    :return: the results of the command
    """
    # Ensure that key is a valid command.
    if key in key_set and key_set[key] in functions:
        return functions[key_set[key]]()
    else:
        raise KeyError("Invalid Command")


def do_commands(stdscr):
    running = True
    while running:
        key = stdscr.getkey()
        try:
            running = execute_command(key)
        except KeyError:
            running = True
