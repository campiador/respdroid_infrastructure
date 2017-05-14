import numpy as np
from matplotlib import pyplot as plt
import matplotlib.patches as mpatches




def createChart(resLists, chart_title, x_label, y_label):

    # print("create chart from output")
    # plt.plot([1, 2, 3, 4])
    # plt.ylabel('some numbers')
    # plt.show()

    for list in resLists:
        if not list:
            "Error: trying to draw empty list"
            exit(1)



    x= ["1", "2", "3", "4"]

    y = [50, 150, 250, 300]
    values_2 = [25, 125, 225, 275]
    values_3 = [1, 111, 11, 12]


    # ax = plt.subplot(111)
    # ax.bar(x, y, color='g', align='center')
    # ax.autoscale(tight=True)

    width = .3

    x_pos = np.arange(len(x))


    y = map(int, y)

    plt.bar(x_pos - width/2, y, width, alpha=0.5, color='r')
    plt.bar(x_pos + width/2, values_2, width, alpha=0.5, color='b')
    # plt.bar(x_pos + 2*width, values_3, width, alpha=0.5, color='g')
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
