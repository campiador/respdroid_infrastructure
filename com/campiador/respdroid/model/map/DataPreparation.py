import matplotlib.pyplot as plt

from com.campiador.respdroid.model import Operations
from com.campiador.respdroid.model.RespNode import RespNode, atomic_get_experiment_number
from com.campiador.respdroid.util import time_and_date, DeviceInfo


class DataPreparation:
    def convertStringToRespImgList(self, imgResultString, experiment_id):
        imgList = []
        for line in imgResultString.splitlines():
            line_elems = line.split("--")
            # print("parsing line: " + str(line_elems))
            # FIXME: a more robost method for detecting respdroid lines needed
            if ("waiting" in line_elems[0] or "beginning" in line_elems[4]):
                # element not a log
                continue
            else:
                # FIXME: this is bug-prone, find a way to avoid magic numbers
                # for index, elem in enumerate(line_elems):
                #     print "line {}:{}".format(index, elem)
                # exit(0)
                respNode = RespNode(0, experiment_id, line_elems[10], line_elems[6], line_elems[2],
                                    Operations.DECODE, line_elems[4], line_elems[5],
                                    line_elems[7], line_elems[8], line_elems[9])
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


def get_dummy_data():
    experiment_id = atomic_get_experiment_number()

    resultLists = [
        [
            RespNode(0, experiment_id, time_and_date.get_current_timestamp(), DeviceInfo.DEVICE_NEXUS_4,
                     60, Operations.DECODE, "sample_img_0", 1, 900, 800, 600),
            RespNode(0, experiment_id, time_and_date.get_current_timestamp(), DeviceInfo.DEVICE_NEXUS_4,
                     120, Operations.DECODE, "sample_img_1", 1, 1000, 900, 700),
            RespNode(0, experiment_id, time_and_date.get_current_timestamp(), DeviceInfo.DEVICE_NEXUS_4,
                     220, Operations.DECODE, "sample_img_2", 1, 1100, 1000, 800),
            RespNode(0, experiment_id, time_and_date.get_current_timestamp(), DeviceInfo.DEVICE_NEXUS_4,
                     320, Operations.DECODE, "sample_img_3", 1, 1200, 1100, 900),
            RespNode(0, experiment_id, time_and_date.get_current_timestamp(), DeviceInfo.DEVICE_NEXUS_4,
                     420, Operations.DECODE, "sample_img_4", 1, 1300, 1200, 1000)
        ],

        [
            RespNode(0, experiment_id, time_and_date.get_current_timestamp(), DeviceInfo.DEVICE_NEXUS_6P,
                     40, Operations.DECODE, "sample_img_0", 1, 900, 800, 600),
            RespNode(0, experiment_id, time_and_date.get_current_timestamp(), DeviceInfo.DEVICE_NEXUS_6P,
                     80, Operations.DECODE, "sample_img_1", 1, 1000, 900, 700),
            RespNode(0, experiment_id, time_and_date.get_current_timestamp(), DeviceInfo.DEVICE_NEXUS_6P,
                     180, Operations.DECODE, "sample_img_2", 1, 1100, 1000, 900),
            RespNode(0, experiment_id, time_and_date.get_current_timestamp(), DeviceInfo.DEVICE_NEXUS_6P,
                     280, Operations.DECODE, "sample_img_3", 1, 1200, 1100, 1000),
            RespNode(0, experiment_id, time_and_date.get_current_timestamp(), DeviceInfo.DEVICE_NEXUS_6P,
                     380, Operations.DECODE, "sample_img_4", 1, 1300, 1200, 1100)
        ]
    ]

    for result_list in resultLists:
        for result in result_list:
            print result.get_json()

    return resultLists


