import matplotlib.pyplot as plt

from com.campiador.respdroid.model import Operations
from com.campiador.respdroid.model.RespNode import RespNode


class DataPreparation:
    def convertStringToRespImgList(self, imgResultString, experiment_id):
        imgList = []
        for line in imgResultString.splitlines():
            line_elems = line.split("--")
            print("parsing line: " + str(line_elems))
            if ("waiting" in line_elems[0] or "beginning" in line_elems[4]):
                # element not a log
                continue
            else:
                # FIXME: this is bug-prone, find a way to avoid magic numbers
                respNode = RespNode(0, experiment_id, line_elems[9], line_elems[6], line_elems[2],
                                    Operations.DECODE, line_elems[4], line_elems[5],
                                    line_elems[7], line_elems[8])
                imgList.append(respNode)

        return imgList

    def imgListTitles(self, imgList):
        titles = []
        for node in imgList:
            titles.append(node.getImageName())
        return titles

    def imgListTitlesAndSizes(self, imgList):
        titles = []
        for node in imgList:
            titles.append("{} ({})".format(node.getImageName(), node.getImgSize()))
        return titles


    def imgListValues(self, imgList):
        values = []
        for node in imgList:
            values.append(node.getTimeDuration())
        return values




