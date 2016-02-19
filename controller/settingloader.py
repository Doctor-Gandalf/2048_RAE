import os
import json
__author__ = 'Kellan Childers'


def get_main_directory(directory_name='2048_RAE'):
    """Find the absolute path to the main directory of application.

    :param directory_name: the name of the main directory (default '2048_RAE')
    :return: the absolute path to the main directory
    """
    full_path = os.path.realpath(__file__)
    directory, file = os.path.split(full_path)

    while file != directory_name:
        directory, file = os.path.split(directory)

    return os.path.join(directory, file)


def read_settings(file):
    """Read a json file in the settings folder.

    :param file: the settings file to read
    :return: the settings in a python dictionary
    """
    directory = get_main_directory()
    os.chdir(directory)

    with open(os.path.join(directory, 'settings', str(file)), 'r') as config_file:
        configs = json.load(config_file)

    return configs
