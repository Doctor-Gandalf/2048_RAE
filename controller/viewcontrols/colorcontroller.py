from curses import init_pair

from ..settingloader import get_main_directory, read_settings
from view.colors import colors
__author__ = 'Kellan Childers'


def create_color_schemes(color_file='colors.config'):
    """Initialize the main color schemes using the settings in a file.

    :param color_file: the file to read color settings from
    :return: null
    """
    color_map = read_settings(color_file)

    for _, color in color_map.items():
        if color not in colors:
            raise KeyError("Could not assign colors")

    # Sets the three main colors for the app screen.
    # First color: text. Second color: background.
    init_pair(1, colors[color_map["primary"]], colors[color_map["secondary"]])
    init_pair(2, colors[color_map["secondary"]], colors[color_map["primary"]])
    init_pair(3, colors[color_map["secondary"]], colors[color_map["tertiary"]])
    init_pair(4, colors[color_map["tertiary"]], colors[color_map["secondary"]])
    init_pair(5, colors[color_map["primary"]], colors[color_map["tertiary"]])
    init_pair(6, colors[color_map["tertiary"]], colors[color_map["primary"]])
