import model.plots as pl

__author__ = 'Kellan Childers'


class Dungeon:
    def __init__(self, width, height):
        """Generate a dungeon.

        :param width: the width of the dungeon
        :param height: the height of the dungeon
        :return: a new dungeon of set size
        """
        self.__background = pl.Plot(width, height)
        self.__midground = pl.Plot(width, height)
        self.__foreground = pl.Plot(width, height)

    def __contains__(self, item):
        """Tell if element is contained in dungeon.

        :param item: the item to search for
        :return: a boolean of if the item is in the plot
        """
        return self.__background.__contains__(item) or \
               self.__midground.__contains__(item) or \
               self.__foreground.__contains__(item)

    def __getitem__(self, item):
        """Get the item at a point in plot.

        :param item: the point in the plot to retrieve from
        :return: the item at the point
        """
        return self.__background[item]

    def __eq__(self, other):
        """Compares plot with another object.

        :param other: the other object to compare
        :return: True if equal, false otherwise
        """
        try:

            return True if self.__background == other.__background or \
                           self.__background == other.__background or \
                           self.__background == other.__background else False
        except AttributeError:
            return False

    def __len__(self):
        """Find the size of the plot.

        :return: the width and height of the plot
        """
        return len(len(self.__background))

    def __str__(self):
        """Generate a user-readable string of plot.

        :return: a string of the elements of the plot
        """
        return '\n'.join(' '.join(str(point) for point in line) for line in self.__background)

    def __repr__(self):
        """Generate a representation of plot.

        :return: a representation of the plot
        """
        return repr(self.__background)
