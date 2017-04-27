import matplotlib.pyplot as plt

from com.campiador.respdroid.model.RespNode import RespNode


class DataPreparation:
    def convertToImageList(self, imgResultString):
        imgList = []
        for line in imgResultString.splitlines():
            line_elems = line.split("--")
            print("parsing line: " + str(line_elems))
            if ("beginning" not in line_elems[4]):
                respNode = RespNode(line_elems[6], line_elems[2], "decode image", line_elems[4], line_elems[5])
                imgList.append(respNode)
            else:
                continue

        return imgList

    def imgListTitles(self, imgList):
        titles = []
        for node in imgList:
            titles.append(node.getBaseParam())
        return titles

    def imgListValues(self, imgList):
        values = []
        for node in imgList:
            values.append(node.getTimeDuration())
        return values