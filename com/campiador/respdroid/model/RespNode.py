# A respnode object corresponds to one line of logcat which in turn represents one operation.
# TODO: all nodes should inherit from an abstract base node, called UX node
import json

import simplejson as simplejson

# TODO: add parameter megapixels
class RespNode:
    def __init__(self, node_id, experiment_id, timestamp, device, delay, operation, imgbase, imgperc, imgsizeKB,
                 img_width, img_height, os_version_release_name, package_name, app_name, app_version_code,
                 activity_name):
        self.activity_name = activity_name
        self.app_version_code = app_version_code
        self.app_name = app_name
        self.package_name = package_name
        self.os_version_release_name = os_version_release_name
        self.node_id = node_id
        self.experiment_id = experiment_id
        self.timestamp = timestamp
        self.device = device
        self.delay = delay
        self.operation = operation
        if ".jpg" in imgbase:
            imgbase = imgbase.replace(".jpg", "")
        self.img_base = imgbase
        self.img_perc = imgperc # FIXME: currently client sends img.length instead!
        self.img_sizeKB = imgsizeKB
        self.imgWidth = int(img_width)
        self.imgHeight = int(img_height)
        self.img_MPs = (self.imgHeight * self.imgWidth) / 1000000.0

    def __str__(self):
        return \
            "nid: " + str(self.node_id) + ", xid: " + str(self.experiment_id) + ", datetime: " + self.timestamp \
             + ", device: " + self.device + ", delay: " + str(self.delay) + ", operation: " + self.operation \
            + ", imgbase: " + self.img_base + ", imgperc: " + str(self.img_perc) + ", "\
               +"sizeKB: " + str(self.img_sizeKB) + ", Resolution: " + self.getImageResolution() \
               + ", MPs: " + str(self.img_MPs) \
            + ", appname:" + self.app_name + ", package_name:" + self.package_name \
            + ", app_version_code:" + str(self.app_version_code) \
            + ", os_version_release_name:" + self.os_version_release_name \
            + ", activity_name:" + self.activity_name

    def __repr__(self):
        return \
            "nid: " + str(self.node_id) + ", xid: " + str(self.experiment_id) + ", datetime: " + self.timestamp \
             + ", device: " + self.device + ", delay: " + str(self.delay) + ", operation: " + self.operation \
            + ", imgbase: " + self.img_base + ", imgperc: " + str(self.img_perc) + ", "\
               +"sizeKB: " + str(self.img_sizeKB) + ", Resolution: " + self.getImageResolution() \
               + ", MPs: " + str(self.img_MPs) \
               + ", appname:" + self.app_name + ", package_name:" + self.package_name \
               + ", app_version_code:" + str(self.app_version_code) \
            + ", os_version_release_name:" + self.os_version_release_name \
            + ", activity_name:" + self.activity_name


    def get_node_id(self):
        return self.node_id

    def getExperimentId(self):
        return self.experiment_id

    def get_timestamp(self):
        return self.timestamp

    def getDevice(self):
        return self.device

    def getTimeDuration(self):
        return self.delay

    def getOperation(self):
        return self.operation

    def getBaseParam(self):
        return self.img_base

    def getScaleParam(self):
        return self.img_perc

    def getImgSize(self):
        return self.img_sizeKB

    def getImageName(self):
        return "{}".format(self.getBaseParam())

    #TODO: handle image resolution
    def getImageResolution(self):
        return str(self.imgWidth)+ "x" + str(self.imgHeight)

    def get_img_width(self):
        return self.imgWidth

    def get_img_height(self):
        return self.imgHeight

    def get_img_megapixels(self):
        return self.img_MPs

    # serialize
    def get_json(self):
        s = json.dumps(self.__dict__) # s set to: {"x":1, "y":2}
        return s
    #
    # def __repr__(self):
    #     print("{}{}".format(self.getBaseParam(), self.getImgSize()))

    # def __str__(self):
    #     print(self.getBaseParam() + "{}".format(self.getImgSize()))


# TODO: use these two to send data from Phone Client to RespDroid Server
    #Serialize
def respnodes_to_json(respnodes):
    s = simplejson.dumps([respnode.__dict__ for respnode in respnodes])
    print s


    # Deserialize
def json_to_respnodes(s):
    clones = simplejson.loads(s)
    print clones
    # Now give our clones some life
    for clone in clones:
        respNode = RespNode()
        respNode.__dict__ = clone
        print respNode
