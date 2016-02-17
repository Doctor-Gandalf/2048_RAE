__author__ = 'Kellan Childers'


class Tile:
    """Represent different elements in a plot as simple values."""

    def __init__(self, value=0):
        """Generate a tile.

        :param value: the main value of the tile
        :return: a new tile with set value and background
        """
        self.value = value

    def __eq__(self, other):
        """Compares tile with another object.

        :param other: the other object to compare
        :return: True if equal, false otherwise
        """
        try:
            if self.value == other.value:
                return True
            else:
                return False
        except AttributeError:
            return False

    def __str__(self):
        """Generate a user-readable string describing tile.

        :return: a string description of tile
        """
        return str(self.value)

    def __repr__(self):
        """Generate a representation of tile.

        :return: a representation of the tile
        """
        return repr(self.value)
