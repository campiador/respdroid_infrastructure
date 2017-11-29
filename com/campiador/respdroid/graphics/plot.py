#  plot.py
#  by Behnam Heydarshahi, October 2017
#  Empirical/Programming Assignment 2
#  COMP 135 Machine Learning
#
#  This module draws charts
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import datetime
import time

import constants

CAPSIZE = 4
PLOT_START = 0
PLOT_END = 1



def plot_accuracies(l_title, l_axis_x, l_axis_y, l1, x1, y1, l2, x2, y2):
    plt.plot(x1, y1, color='r', label=l1)
    plt.plot(x1, y1, 'ro')

    plt.plot(x2, y2, color='b', label=l2)
    plt.plot(x2, y2, 'bs')

    plt.title(l_title)
    plt.xlabel(l_axis_x)
    plt.ylabel(l_axis_y)

    plt.axis([0, 100, 0, 100])
    plt.legend(loc='best')
    plt.show(block=False)
    plt.savefig('./part1_accuracies.png')



def plot_accuracies_with_stderr(l_title, l_axis_x, l_axis_y, l1, x1, y1, y1err, l2, x2, y2, y2err,
                                l3, x3, y3, y3err, l4, x4, y4, y4err):

    plt.errorbar(x1,  y1, yerr=y1err, color='r', label=l1, capsize=CAPSIZE)
    plt.plot(x1, y1, 'ro')

    plt.errorbar(x2,  y2, yerr=y2err, color='b', label=l2, capsize=CAPSIZE)
    plt.plot(x2, y2, 'bo')

    plt.errorbar(x3,  y3, yerr=y3err, color='g', label=l3, capsize=CAPSIZE)
    plt.plot(x3, y3, 'gs')

    plt.errorbar(x4,  y4, yerr=y4err, color='y', label=l4, capsize=CAPSIZE)
    plt.plot(x4, y4, 'ys')

    plt.title(l_title)
    plt.xlabel(l_axis_x)
    plt.ylabel(l_axis_y)

    plt.axis([0, 550, 0, 100])
    plt.legend(loc='best')
    plt.show(block=False)
    plt.savefig('./output/hw1_part_2_accuracies_with_stderr.png')


#plotables
#l1_list, x1_list, y1_list, y1err_list

# Credits: https://stackoverflow.com/questions/14720331/how-to-generate-random-colors-in-matplotlib
def get_cmap(n, name='hsv'):
    '''Returns a function that maps each index in 0, 1, ..., n-1 to a distinct
    RGB color; the keyword argument name must be a standard mpl colormap name.'''
    return plt.cm.get_cmap(name, n)


def plot_accuracies_with_stderr_poly(main_title, x_axis_tile, y_axis_title, range_x, range_y, subplotables,
                                     output_file_name):
    cmap = get_cmap(len(subplotables) + 1)

    for i, plotable in enumerate(subplotables):
        color = cmap(i)
        if constants.DEBUG_VERBOSE:
            print " color {} = {}".format(i, color)

        # Values and errors
        plt.errorbar(plotable.x_values, plotable.y_values, plotable.y_std_err_values, color=color,
                     label=plotable.label, capsize=CAPSIZE)

        # the dots
        # plt.plot(plotable.x_values, plotable.y_values, )

    plt.title(main_title)
    plt.xlabel(x_axis_tile)
    plt.ylabel(y_axis_title)

    plt.axis([range_x[PLOT_START], range_x[PLOT_END], range_y[PLOT_START], range_y[PLOT_END]])
    plt.legend(loc='best')

    # BUG:
    # When I show(block=False) or don't show() at all, the plt object somehow does not die and what happens is
    # the past plots are not discarded when drawing new plots.
    # When I show(block=True), the image does not get saved!

    # BUG FIX 1:
    # First save, then show(block = True)

    # BUG FIX 2:
    # Even better: after show(block=false)  call plt.gcf().clear(). Also might call plt.clf() plt.cla() plt.close().


    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    plt.savefig('./output/{}_{}_{}.png'.format(output_file_name, main_title, st))

    plt.show(block=False)
    plt.gcf().clear()

