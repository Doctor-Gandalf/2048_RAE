#!/usr/bin/python3
import os
import controller.settingloader as sl

__author__ = 'Kellan Childers'

if __name__ == "__main__":
    os.chdir(sl.get_main_directory())
    print('Hello world')
