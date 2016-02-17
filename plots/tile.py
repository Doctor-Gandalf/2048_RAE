__author__ = 'Kellan Childers'


class Tile:
    """Represent different elements in a plot as simple values."""
    def __init__(self, value=0, background="white"):
        """Generate a tile.

        :param value: the main value of the tile
        :param background: the background color of the tile
        :return: a new tile with set value and background
        """
        self.value = value
        self.background = background

    def __eq__(self, other):
        """Compares tile with another object.

        :param other: the other object to compare
        :return: True if equal, false otherwise
        """
        try:
            if self.value == other.value and self.background == other.background:
                return True
            else:
                return False
        except AttributeError:
            return False

    def __add__(self, other):
        """Add two equal value tiles together.

        :param other: the tile to add to the current tile
        :return: the next tile in the sequence
        """
        if self == other:
            return Tile(2 * self.value, background=str(2 * self.value))
        else:
            raise TypeError('Cannot add two tiles of differing value')

    def __str__(self):
        """Generate a user-readable string describing tile.

        :return: a string description of tile
        """
        return str(self.value)

    def __repr__(self):
        """Generate a representation of tile.

        :return: a representation of the tile
        """
        return repr(self.value) + ' ' + repr(self.background)
