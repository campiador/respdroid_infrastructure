import matplotlib.pyplot as plt

from com.campiador.respdroid.model.RespNode import RespNode


class DataPreparation:
    def convertStringToImageList(self, imgResultString):
        imgList = []
        for line in imgResultString.splitlines():
            line_elems = line.split("--")
            print("parsing line: " + str(line_elems))
            if ("waiting" in line_elems[0] or "beginning" in line_elems[4]):
                # element not a log
                continue
            else:

                respNode = RespNode(line_elems[6], line_elems[2], "decode image", line_elems[4], line_elems[5],
                                    line_elems[7])
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




