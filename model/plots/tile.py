__author__ = 'Kellan Childers'


class Tile:
    """Represent different elements in a plot as simple values."""

    def __init__(self, value=0):
        """Generate a tile.

        :param value: the main value of the tile (default 0)
        :return: a new tile with set value and background
        """
        self.__value = value

    def __add__(self, other):
        """Add two tiles of the same type together.

        :param other: the other tile to add
        :type other: Tile
        :return: the next tile in the sequence
        """
        if self == other:
            pass
        else:
            raise ValueError("Cannot add two non-equal tiles.")

    def __eq__(self, other):
        """Compares tile with another object.

        :param other: the other object to compare
        :return: True if equal, false otherwise
        """
        try:
            if self.__value == other.__value:
                return True
            else:
                return False
        except AttributeError:
            # Accounts for comparisons to non-Tile objects.
            return False

    def __str__(self):
        """Generate a user-readable string describing tile.

        :return: a string description of tile
        """
        return str(self.__value)

    def __repr__(self):
        """Generate a representation of tile.

        :return: a representation of the tile
        """
        return repr(self.__value)
