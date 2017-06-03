# TODO: all nodes should inherit from an abstract base node, called UX node
from com.campiador.respdroid.util import PersistentData


class RespNode:
    def __init__(self, node_id, experiment_id, timestamp, device, delay, operation, imgbase, imgperc, imgsizeKB):
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
        return "not yet"
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