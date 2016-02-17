import os
import json
__author__ = 'Kellan Childers'


def get_main_directory():
    full_path = os.path.realpath(__file__)
    directory, file = os.path.split(full_path)

    while file != '2048_Rogue':
        directory, file = os.path.split(directory)

    return os.path.join(directory, file)


def read_settings(file):
    directory = get_main_directory()
    os.chdir(directory)

    with open(os.path.join(directory, 'settings', str(file)), 'r') as config_file:
        configs = json.load(config_file)

    return configs
