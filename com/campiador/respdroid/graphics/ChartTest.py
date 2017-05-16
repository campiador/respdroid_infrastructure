import numpy as np
from matplotlib import pyplot as plt
import matplotlib.patches as mpatches

from com.campiador.respdroid.util.DataPreparation import DataPreparation

import matplotlib.cm as cmx
import matplotlib.colors as colors

def get_cmap(N):
    '''Returns a function that maps each index in 0, 1, ... N-1 to a distinct 
    RGB color.'''
    color_norm  = colors.Normalize(vmin=0, vmax=N-1)
    scalar_map = cmx.ScalarMappable(norm=color_norm, cmap='hsv')
    def map_index_to_rgb_color(index):
        return scalar_map.to_rgba(index)
    return map_index_to_rgb_color

def createChart(resLists, chart_title, x_label, y_label):

    # print("create chart from output")
    # plt.plot([1, 2, 3, 4])
    # plt.ylabel('some numbers')
    # plt.show()

    for list in resLists:
        if not list:
            "Error: trying to draw empty list"
            exit(1)

    N_devices = len(resLists)
    cmap = get_cmap(N_devices)
    for i in range(N_devices):
        print cmap(i)

    #TODO: check to make sure all x value lists are identical
    for i, resList in enumerate(resLists):
        x_temp = DataPreparation().imgListTitles(resList)
        y_temp = DataPreparation().imgListValues(resList)

        N_datapoints = len(x_temp)

        width = 1 / float(N_datapoints + 1)

        col = cmap(i)
        x_pos = np.arange(N_datapoints)

        y = map(int, y_temp)

        plt.bar(x_pos + width * float(i), y_temp, width, alpha=0.5, color=col)

    # ax = plt.subplot(111)
    # ax.bar(x, y, color='g', align='center')
    # ax.autoscale(tight=True)




    plt.xticks(x_pos, x)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(chart_title)
    threshold_soft = 100.0
    threshold_hard = 200.0

    # plt.legend([y], [label])
    # plt.legend(handles=[plt])

    plt.plot([0., 4.5], [threshold_soft, threshold_soft], "k--")
    plt.plot([0., 4.5], [threshold_hard, threshold_hard], "k--")

    red_patch = mpatches.Patch(color='r', label='The red data')
    blue_patch = mpatches.Patch(color='b', label='The blue data')
    plt.legend(handles=[red_patch, blue_patch])


    plt.show()


# createChart([], "chart title", "x axis label", "y_axis_label")
