import json

import matplotlib.pyplot as plt
import re

from com.campiador.respdroid.model import Operations
from com.campiador.respdroid.model.RespNode import RespNode
from com.campiador.respdroid.model.responode_factory import deserialize_json_to_respnode, deserialize_dict_to_respnode
from com.campiador.respdroid.util import time_and_date, DeviceInfo
from com.campiador.respdroid.util.json_helper import is_valid_json


def deserializeStringsToRespnodes(logcat_lines_including_serialized_respnodes, experiment_id):
    print("deserialize started")
    respNodes = []
    for line in logcat_lines_including_serialized_respnodes.splitlines():
        # print("\n")
        # line_elems = line.split("--")
        # # print("parsing line: " + str(line_elems))
        # # FIXME: a more robost method for detecting respdroid lines needed
        # if ("waiting" in line_elems[0] or "beginning" in line_elems[4]):
        #     # element not a log
        #     continue
        # else:
        #     # FIXME: this is bug-prone, find a way to avoid magic numbers
        #     # for index, elem in enumerate(line_elems):
        #     #     print "line {}:{}".format(index, elem)
        #     # exit(0)
        #
        #     # respNode = RespNode(0, experiment_id, line_elems[10], line_elems[6], line_elems[2],
        #     #                     Operations.DECODE, line_elems[4], line_elems[5],
        #     #                     line_elems[7], line_elems[8], line_elems[9])
        #     # respNodes.append(respNode)

        if "{" in line: #probably json
            # print "line is probably valid json"
            # print line
            # remove the logcat info in front of the log
            sanitized_line = re.sub(r'.*{', '{', line)
            # print "sanitized line:"
            # print sanitzed_line
            if is_valid_json(sanitized_line):
                # print("valid json")
                # print(sanitized_line)
                dct = json.loads(sanitized_line)
                respNode = deserialize_dict_to_respnode(dct)
                # print str(respNode.getImageResolution())
                # print respNode
                # the client device does not know the experiment ID. We know it
                respNode.experiment_id = experiment_id
                respNodes.append(respNode)
            else:
                # print("bad json format:")
                # print(sanitzed_line)
                print("waring: line starts with \{ but is not json")
        else:
            # print("line was useless logcat")
            ""
    print("deserialize ended")
    for node in respNodes:
        print node
    return respNodes


def imgListTitles(imgList):
    titles = []
    for node in imgList:
        titles.append(node.getImageName())
    return titles

def imgListTitlesAndSizes(imgList):
    titles = []
    for node in imgList:
        titles.append("{} ({})".format(node.getImageName(), node.getImgSize()))
    return titles


def imgs_title_and_mp(imgs):
    titles_mps = []
    for node in imgs:
        titles_mps.append("{}({})".format(node.getImageName(), node.get_img_megapixels()))
    return titles_mps


def imgListValues(imgList):
    values = []
    for node in imgList:
        values.append(node.getTimeDuration())
    return values


def get_dummy_data(experiment_id):

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

    return resultLists


def partition_nodelist_by_device_type_return_sublists(node_list):
    # [[device_1_nodes], [device_2_nodes], ...]
    sublists = []

    seen_device_types = []

    for respnode in node_list:
        node_device_type = respnode.getDevice()
        if node_device_type not in seen_device_types:
            # First node with this device type
            seen_device_types.append(node_device_type)
            sublists.append([])

        device_type_index = seen_device_types.index(node_device_type)
        # find the sublist for device type and add the node to it
        sublists[device_type_index].append(respnode)

    return sublists



