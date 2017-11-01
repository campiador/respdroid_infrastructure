import matplotlib.colors as colors
import matplotlib.patches as mpatches
import numpy as np
from matplotlib import pyplot as plt


# def get_cmap(N):
#     '''Returns a function that maps each index in 0, 1, ... N-1 to a distinct
#     RGB color.'''
#     color_norm  = colors.Normalize(vmin=0, vmax=N-1)
#     scalar_map = cmx.ScalarMappable(norm=color_norm, cmap='hsv')
#     def map_index_to_rgb_color(index):
#         return scalar_map.to_rgba(index)
#     return map_index_to_rgb_color
from com.campiador.respdroid.model.map import DataPreparation
from com.campiador.respdroid.util import Config

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

    # CONTINUE HERE: FIXME: why TypeError: iteration over non-sequence? prepare for boxplot. write a create box plot
    # TODO: check to make sure all x value lists are identical
    for i, resList in enumerate(resLists):
        x_temp = DataPreparation.imgListTitlesAndSizes(resList)
        y_temp = DataPreparation.imgListValues(resList)

        N_datapoints = len(x_temp)

        device_type = resList[i].getDevice()

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
    plt.show(block=Config.RESULT_CHART_BLOCKS)
    # plt.show()

    #plt.savefig('./{}'.format(date.ctime()))

def create_box_chart_x1(resList, chart_title, x_label, y_label):
    # fake up some data
    # spread = np.random.rand(50) * 100
    # center = np.ones(25) * 50
    # flier_high = np.random.rand(10) * 100 + 100
    # flier_low = np.random.rand(10) * -100

    y_data = [node.getTimeDuration() for node in resList]
    y_data = map(int, y_data)

    x_data = [resList[0].getImgSize()]

    # data = np.concatenate((spread, center, flier_high, flier_low), 0)
    print x_data

    # # fake up some more data
    # spread = np.random.rand(50) * 100
    # center = np.ones(25) * 40
    # flier_high = np.random.rand(10) * 100 + 100
    # flier_low = np.random.rand(10) * -100
    # d2 = np.concatenate((spread, center, flier_high, flier_low), 0)
    # data.shape = (-1, 1)
    # d2.shape = (-1, 1)
    #
    # # data = concatenate( (data, d2), 1 )
    # # Making a 2-D array only works if all the columns are the
    # # same length.  If they are not, then use a list instead.
    # # This is actually more efficient because boxplot converts
    # # a 2-D array into a list of vectors internally anyway.
    # data = [data, d2, d2[::2, 0]]

    print y_data
    #


    # basic plot
    plt.figure()
    plt.boxplot(y_data, 0, 'gD', positions=x_data)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(chart_title)

    plt.show()

    ""
# createChart([], "chart title", "x axis label", "y_axis_label")
def x2_createChart(resLists, chart_title, x_label, y_label):
    for list in resLists:
        if not list:
            "Error: trying to draw empty list"
            exit(1)
    legend_patches = []

    # CONTINUE HERE: FIXME: why TypeError: iteration over non-sequence? prepare for boxplot. write a create box plot
    # TODO: check to make sure all x value lists are identical
    for i, resList in enumerate(resLists):
        x_temp = DataPreparation.imgListTitlesAndSizes(resList)
        y_temp = DataPreparation.imgListValues(resList)

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
    plt.show(block=Config.RESULT_CHART_BLOCKS)
    # plt.show()

    #plt.savefig('./{}'.format(date.ctime())


    ""


# createChart([], "chart title", "x axis label", "y_axis_label")
def plot_with_error_bars(resLists, chart_title, x_label, y_label):
    for list in resLists:
        if not list:
            "Error: trying to draw empty list"
            exit(1)
    legend_patches = []

    # CONTINUE HERE: FIXME: why TypeError: iteration over non-sequence? prepare for boxplot. write a create box plot
    # TODO: check to make sure all x value lists are identical
    for i, resList in enumerate(resLists):
        x_sub = DataPreparation.imgs_title_and_mp(resList)
        y_sub = DataPreparation.imgListValues(resList)
        y_error = [respnode.std_error for respnode in resList]
        N_datapoints = len(x_sub)

        device_type = resList[0].getDevice()

        width = 1 / float(N_datapoints + 1)

        col = get_a_color(i)
        x_pos = np.arange(N_datapoints)

        # y = map(int, y_temp)

        # print "index is {} and color is {}".format(i, col)
        # plt.bar(x_pos + width * float(i), y_sub, width, alpha=1, color=col)
        # plt.errorbar(x_pos + width * float(i), y_sub, yerr=y_error, color='b', label=l2, capsize=CAPSIZE)
        plt.errorbar(x_pos, y_sub, color=col, yerr=y_error, capsize=5)

        patch = mpatches.Patch(color=col, label=device_type)
        legend_patches.append(patch)

    plt.xticks(x_pos, x_sub)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(chart_title)

    # set responsiveness bars
    threshold_soft = 100.0
    threshold_hard = 200.0
    plt.plot([0., 4.5], [threshold_soft, threshold_soft], "k--")
    plt.plot([0., 4.5], [threshold_hard, threshold_hard], "k--")

    plt.legend(handles=legend_patches)

    # TODO: we want the code to flow after drawing a chart. show() blocks by default.
    plt.show(block=Config.RESULT_CHART_BLOCKS)
    # plt.show()

    # plt.savefig('./{}'.format(date.ctime())