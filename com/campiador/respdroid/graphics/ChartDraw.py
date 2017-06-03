import datetime
import time

import numpy as np
from matplotlib import pyplot as plt
import matplotlib.patches as mpatches

from com.campiador.respdroid.util.DataPreparation import DataPreparation

import matplotlib.cm as cmx
import matplotlib.colors as colors

# def get_cmap(N):
#     '''Returns a function that maps each index in 0, 1, ... N-1 to a distinct
#     RGB color.'''
#     color_norm  = colors.Normalize(vmin=0, vmax=N-1)
#     scalar_map = cmx.ScalarMappable(norm=color_norm, cmap='hsv')
#     def map_index_to_rgb_color(index):
#         return scalar_map.to_rgba(index)
#     return map_index_to_rgb_color

colors = ['r', 'b', 'g', 'y']

def get_a_color(i):
    max = len(colors)
    if i >= max:
        print("We only have {} colors. {} is too many.\n Please extend get_a_color func".format(max, i))
        exit(1)
    return colors[i]


def createChart(resLists, chart_title, x_label, y_label):
    for list in resLists:
        if not list:
            "Error: trying to draw empty list"
            exit(1)
    legend_patches = []

    # TODO: check to make sure all x value lists are identical
    for i, resList in enumerate(resLists):
        x_temp = DataPreparation().imgListTitlesAndSizes(resList)
        y_temp = DataPreparation().imgListValues(resList)

        N_datapoints = len(x_temp)

        device_type = resList[0].getDevice()

        width = 1 / float(N_datapoints + 1)

        col = get_a_color(i)
        x_pos = np.arange(N_datapoints)

        y = map(int, y_temp)

        # print "index is {} and color is {}".format(i, col)
        plt.bar(x_pos + width * float(i), y_temp, width, alpha=1, color=col)

        patch = mpatches.Patch(color=col, label=device_type)
        legend_patches.append(patch)

    plt.xticks(x_pos, x_temp)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(chart_title)

    #set responsiveness bars
    threshold_soft = 100.0
    threshold_hard = 200.0
    plt.plot([0., 4.5], [threshold_soft, threshold_soft], "k--")
    plt.plot([0., 4.5], [threshold_hard, threshold_hard], "k--")


    plt.legend(handles=legend_patches)

    # TODO: we want the code to flow after drawing a chart. show() blocks by default.
    # plt.show(block=False)
    plt.show()

    #plt.savefig('./{}'.format(date.ctime()))


# createChart([], "chart title", "x axis label", "y_axis_label")
