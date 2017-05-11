class RespNode:
    def __init__(self, device, time, operation, imgbase, imgperc, imgsizeKB):
        self.device = device
        self.time = time
        self.operation = operation
        if ".jpg" in imgbase:
            imgbase = imgbase.replace(".jpg", "")
        self.img_base = imgbase
        self.img_perc = imgperc
        self.img_sizeKB = imgsizeKB

    def getDevice(self):
        return self.device

    def getTimeDuration(self):
        return self.time

    def getOperation(self):
        return self.operation

    def getBaseParam(self):
        return self.img_base

    def getScaleParam(self):
        return self.img_perc

    def getImgSize(self):
        return self.img_sizeKB
