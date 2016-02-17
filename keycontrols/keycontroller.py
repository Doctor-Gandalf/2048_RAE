from ..settingloader import read_settings
from .functiondict import functions
__author__ = 'Kellan Childers'


def execute_command(key, key_file='keybindings.config'):
    """Execute a key command based on a key binding.

    :param key: the key command to execute
    :param key_file: the file to base commands on
    :return: the results of the command
    """
    keys = read_settings(key_file)

    # Ensure that key is a valid command.
    if key in keys and keys[key] in functions:
        return functions[keys[key]]()
    else:
        raise KeyError("Invalid Command")
