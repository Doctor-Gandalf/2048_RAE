#!/usr/bin/python3
from json import load, dump
from model.plots.plot import Plot

__author__ = 'Kellan Childers'


def points(width, height):
    """Convenience iterator to work with points in a plot.
    Note: width and height must be both ints or lists, not of mixed type.

    :param width: the width of the plot
    :param height: the height of the plot
    :return: an iterator over the points
    """
    if isinstance(width, type([])):
        # Check if width and height are sequences.
        for outer_val in range(*height):
            for inner_val in range(*width):
                yield inner_val, outer_val
    else:
        # Width and height are ints and can be handled normally.
        for outer_val in range(height):
            for inner_val in range(width):
                yield inner_val, outer_val


def points_of(plot):
    """Iterate over a plot without needing to know its width and height.

    :param plot: the plot to iterate over
    :return: an iterator over the points
    """
    return points(*(get_dimensions(plot)))


def get_dimensions(plot):
    """Get the width and height of the plot.

    :param plot: the plot to measure
    :return: the width and height as a tuple
    """
    return len(plot), len(plot[0])


def positive_integer(value):
    """Force value to be a positive integer

    :param value: the value to test
    :return: the value if it is positive
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

    for i, j in points([-1, 2], [-1, 2]):
        try:
            surround_list += [plot[x + i, y + j]] if x + i >= 0 and y + j >= 0 else []
        except IndexError:
            pass

    try:
        surround_list.remove(plot[x, y])
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

    plot = Plot(*(get_dimensions(reader)))
    for x, y in points_of(plot):
        plot[x, y] = reader[x][y]

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
    new_plot = Plot(*(get_dimensions(plot)))

    for x, y in points_of(plot):
        new_plot[x, y] = plot[x, y]

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

    for x, y in points_of(plot):
        try:
            new_plot[x, y] = plot[x, y]
        except IndexError:
            # Dimensions are smaller than before and elements can be skipped.
            pass

    return new_plot


def clear(plot):
    """Make a plot of equal size, clear of all entries.

    :param plot: the plot to clear
    :return: a cleared plot
    """
    return Plot(*(get_dimensions(plot)))


if __name__ == "__main__":
    demo_plot = Plot(4, 4)
    for example_x, example_y in points_of(demo_plot):
        demo_plot[example_x, example_y] = example_x + example_y

    print('Demoing Plot operations:\n\nShowing demo 4x4 plot.')
    print(demo_plot)

    print('\nShowing ability to copy plot.')
    print(copy(demo_plot))

    print('\nShowing ability to find elements around (1, 3)')
    print(surrounding(demo_plot, (1, 3)))

    print('\nShowing ability to resize plot to 5x5.')
    demo_plot = resize(demo_plot, (5, 5))
    print(demo_plot)

    print('\nShowing ability to resize plot to 3x3.')
    demo_plot = resize(demo_plot, (3, 3))
    print(demo_plot)

    print('\nShowing ability to clear plot.')
    demo_plot = clear(demo_plot)
    print(demo_plot)
