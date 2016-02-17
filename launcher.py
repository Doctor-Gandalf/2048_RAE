#!/usr/bin/python3
import os
import controller.settingloader as sl
import model.dungeons as dng

__author__ = 'Kellan Childers'

if __name__ == "__main__":
    os.chdir(sl.get_main_directory())
    test_dungeon = dng.Dungeon(4, 4)
    print(test_dungeon)
