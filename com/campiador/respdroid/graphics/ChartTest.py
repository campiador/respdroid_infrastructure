import numpy as np
from matplotlib import pyplot as plt
import matplotlib.patches as mpatches

from com.campiador.respdroid.util.DataPreparation import DataPreparation


def createChart(resLists, chart_title, x_label, y_label):

    # print("create chart from output")
    # plt.plot([1, 2, 3, 4])
    # plt.ylabel('some numbers')
    # plt.show()

    for list in resLists:
        if not list:
            "Error: trying to draw empty list"
            exit(1)

    x = ["1", "2", "3", "4"]

    for resList in resLists:
        x_temp = DataPreparation().imgListTitles(resList)
        for index, value in enumerate(x):
            print index,"-",value
            if  (x[index] == value):
                # CONTINUE
            else:
                print "big problem
                exit(1)


        y = DataPreparation().imgListValues(resList)
        for index, j in enumerate(y):
            print index, "-", j





    y = [50, 150, 250, 300]
    values_2 = [60, 165, 275, 310]
    values_3 = [80, 175, 290, 320]


    # ax = plt.subplot(111)
    # ax.bar(x, y, color='g', align='center')
    # ax.autoscale(tight=True)

    width = 1 / float(len(x) + 1)

    x_pos = np.arange(len(x))


    y = map(int, y)

    plt.bar(x_pos + width * float(0), y, width, alpha=0.5, color='r')
    plt.bar(x_pos + width * float(1), values_2, width, alpha=0.5, color='b')
    plt.bar(x_pos + width * float(2), values_3, width, alpha=0.5, color='g')
    plt.bar(x_pos + width * float(3), values_3, width, alpha=0.5, color='y')

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
