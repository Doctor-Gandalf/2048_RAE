from json import load, dump

from model.plots.plot import Plot

__author__ = 'Kellan Childers'


def point_iterator(width, height):
    """Convenience iterator to work with points in a plot.

    :param width: the width of the plot
    :param height: the height of the plot
    :return: an iterator over the points
    """
    for x in range(width):
        for y in range(height):
            yield x, y


def positive_integer(value):
    """Force value to be a positive integer

    :param value: The value to test
    :return: The value if it is positive
    """
    if value < 0:
        raise TypeError("Argument must be positive integer")
    return value


def surrounding(plot, point):
    """Get all elements surrounding a point on a plot.

    :param plot: the plot to operate on
    :type plot: Plot
    :param point: the point on the plot to surround
    :return: a list of all elements surrounding the point
    """
    x, y = map(positive_integer, point)
    surround_list = []

    for i in range(-1, 2):
        for j in range(-1, 2):
            try:
                surround_list += [plot[x+i][y+j]] if x+i >= 0 and y + j >= 0 else []
            except IndexError:
                pass

    try:
        surround_list.remove(plot[x][y])
    except ValueError:
        # (x, y) wasn't in the plot and can be ignored.
        pass

    return surround_list


def read_from_file(filename):
    """Read a json file and load the graph from it.

    :param filename: the name of the file to be read
    :return: the newly created plot
    """
    with open(filename, 'r') as read_file:
        reader = load(read_file)

    plot = Plot(len(reader), len(reader[0]))
    for x in range(len(reader)):
        for y in range(len(reader[0])):
            plot[x][y] = reader[x][y]

    return plot


def save_to_file(plot, filename):
    """Save the graph to a json file.
    Note: This function has side effects.

    :param plot: the plot to operate on
    :type plot: Plot
    :param filename: the name of the file to be written to
    :return: null
    """
    writer = [[point for point in line] for line in plot]
    with open(filename, 'w') as write_file:
        dump(writer, write_file)


def copy(plot):
    """Copy the plot to a new location.

    :param plot: the plot to copy
    :type plot: Plot
    :return: a copy of the graph
    """
    new_plot = Plot(len(plot), len(plot[0]))

    for x in range(len(plot)):
        for y in range(len(plot[0])):
            new_plot[x][y] = plot[x][y]

    return new_plot


def resize(plot, new_dimensions, fill=None):
    """Make a new plot with elements from the plot.

    :param plot: the plot to copy and resize
    :type plot: Plot
    :param new_dimensions: the new dimensions of the plot
    :param fill: the default value for any elements not in the original plot (default None)
    :return: the new plot
    """
    width, height = map(positive_integer, new_dimensions)

    # This is avoids the try-except loop.
    if width == len(plot) and height == len(plot[0]):
        return copy(plot)

    new_plot = Plot(width, height, fill)

    for x in range(len(plot)):
        for y in range(len(plot[0])):
            try:
                new_plot[x][y] = plot[x][y]
            except IndexError:
                # Dimensions are smaller than before and elements can be skipped.
                pass

    return new_plot

if __name__ == "__main__":
    demo_plot = Plot(4, 4)
    for x, y in point_iterator(len(demo_plot[0]), len(demo_plot)):
        demo_plot[x, y] = x + y
    print(demo_plot)
