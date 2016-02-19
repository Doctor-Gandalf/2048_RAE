__author__ = 'Kellan Childers'


class Plot:
    """Basic class to allow default operations on plots."""

    def __init__(self, width, height, fill=None):
        """Generate a plot.

        :param width: the width of the plot
        :param height: the height of the plot
        :param fill: the elements of the plot (default None)
        :return: a new plot of fill elements and set dimensions
        """
        self.__plot = [[fill for _ in range(height)] for _ in range(width)]

    def __contains__(self, item):
        """Tell if element is contained in plot.

        :param item: the item to search for
        :return: a boolean of if the item is in the plot
        """
        contains = False
        for line in self.__plot:
            contains += line.__contains__(item)
        return bool(contains)

    def __getitem__(self, item):
        """Get the item at a point in plot.

        :param item: either a point or a row in the plot to retrieve
        :return: the item at the point
        """
        if isinstance(item, type(1)):
            # This is needed for finding the height of the plot.
            return self.__plot[item]
        elif isinstance(item, type((1, 1))):
            # The back-end data is held in a (y, x) coordinate system and has to reverse front-end calls.
            return self.__plot[item[1]][item[0]]
        else:
            raise TypeError("plot indices must be either integers or tuples, not " + str(item.__class__.__name__))

    def __setitem__(self, key, value):
        """Set the item at a point in plot.

        :param key: the point in the plot to set
        :param value: the item at the point
        :return: null
        """
        if isinstance(key, type((1, 1))):
            # The back-end data is held in a (y, x) coordinate system and has to reverse front-end calls.
            self.__plot[key[1]][key[0]] = value
        else:
            raise TypeError("plot indices must be tuples, not " + str(key.__class__.__name__))

    def __eq__(self, other):
        """Compares plot with another object.

        :param other: the other object to compare
        :return: True if equal, false otherwise
        """
        try:
            return True if self.__plot == other.__plot else False
        except AttributeError:
            # Accounts for non-Plot objects.
            return False

    def __len__(self):
        """Find the size of the plot.

        :return: the width and height of the plot
        """
        return len(self.__plot)

    def __iter__(self):
        """Iterate over all values in plot.

        :return: an iterator over the values
        """
        for y in range(len(self.__plot)):
            for x in range(len(self.__plot[0])):
                yield self.__plot[y][x]

    def __str__(self):
        """Generate a user-readable string of plot.

        :return: a string of the elements of the plot
        """
        return '\n'.join(' '.join(str(point) if point is not None else 'N' for point in line)
                         for line in self.__plot)

    def __repr__(self):
        """Generate a representation of plot.

        :return: a representation of the plot
        """
        return repr(self.__plot)


if __name__ == "__main__":
    demo_plot = Plot(4, 4)

    print('Demoing Plot type:\n\nShowing default 4x4 plot.')
    print(demo_plot)

    print('\nShowing plot equals a new 4x4 plot.')
    print(demo_plot == Plot(4, 4))

    print('\nShowing setting point (1, 2) to 5.')
    demo_plot[1, 2] = 5
    print(demo_plot)

    print('\nShowing plot contains 5.')
    print(demo_plot.__contains__(5))

    print('\nShowing computer representation of plot.')
    print(repr(demo_plot))
