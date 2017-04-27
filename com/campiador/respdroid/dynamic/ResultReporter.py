from matplotlib import pyplot as plt
import numpy as np

from com.campiador.respdroid.util.DataPreparation import DataPreparation


class ResultReporter:
    def createChart(self, resList):

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

        plt.bar(y_pos, y, align='center', alpha=0.5)
        plt.xticks(y_pos, x)
        plt.ylabel('Time in milliseconds')
        plt.title('Image File')
        plt.show()
