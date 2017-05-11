from matplotlib import pyplot as plt
import numpy as np

from com.campiador.respdroid.util.DataPreparation import DataPreparation


class ResultReporter:
    def createChart(self, resList, label):

        # print("create chart from output")
        # plt.plot([1, 2, 3, 4])
        # plt.ylabel('some numbers')
        # plt.show()

        x = DataPreparation().imgListTitles(resList)
        for i in x:
            print i



        y = DataPreparation().imgListValues(resList)
        for j in y:
            print j

        # ax = plt.subplot(111)
        # ax.bar(x, y, color='g', align='center')
        # ax.autoscale(tight=True)

        y_pos = np.arange(len(x))

        y = map(int, y)

        plt.bar(y_pos, y, align='center', alpha=0.5, color='r')
        plt.xticks(y_pos, x)
        plt.ylabel('Time in milliseconds')
        plt.xlabel('Image File')
        plt.title('Responsiveness')
        threshold_soft = 100.0
        threshold_hard = 200.0

        plt.legend([y], [label])
        # plt.legend(handles=[plt])

        plt.plot([0., 4.5], [threshold_soft, threshold_soft], "k--")
        plt.plot([0., 4.5], [threshold_hard, threshold_hard], "k--")

        plt.show()
