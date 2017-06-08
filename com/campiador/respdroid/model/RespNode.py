# A respnode object corresponds to one line of logcat which in turn represents one operation.
# TODO: all nodes should inherit from an abstract base node, called UX node
import json

from com.campiador.respdroid.storage import PersistentData

# TODO: add parameter megapixels
class RespNode:
    def __init__(self, node_id, experiment_id, timestamp, device, delay, operation, imgbase, imgperc, imgsizeKB,
                 img_width, img_height):
        self.node_id = node_id
        self.experiment_id = experiment_id
        self.timestamp = timestamp
        self.device = device
        self.delay = delay
        self.operation = operation
        if ".jpg" in imgbase:
            imgbase = imgbase.replace(".jpg", "")
        self.img_base = imgbase
        self.img_perc = imgperc
        self.img_sizeKB = imgsizeKB
        self.imgWidth = img_height
        self.imgHeight = img_width
        self.img_MPs = (self.imgHeight * self.imgWidth) / 1000000.0

    def __str__(self):
        return "nid: " + str(self.node_id) + ", xid: " + str(self.experiment_id) + ", datetime: " + self.timestamp \
             + ", device: " + self.device + ", delay: " + self.delay + ", operation: " + self.operation + \
               ", imgbase: " + self.img_base + ", imgperc: " + str(self.img_perc) + ", sizeKB: " \
               + str(self.img_sizeKB) + ", Resolution: " + self.getImageResolution() + ", MPs: " + str(self.img_MPs)

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

    def get_json(self):
        s = json.dumps(self.__dict__) # s set to: {"x":1, "y":2}
    #
    # def __repr__(self):
    #     print("{}{}".format(self.getBaseParam(), self.getImgSize()))

    # def __str__(self):
    #     print(self.getBaseParam() + "{}".format(self.getImgSize()))

def atomic_get_experiment_number():
    # FIXME: the next three lines should be ideally atomic
    experiment_number = PersistentData.load_experiment_id()
    experiment_number += 1
    PersistentData.save_experiment_id(experiment_number)
    return experiment_number
