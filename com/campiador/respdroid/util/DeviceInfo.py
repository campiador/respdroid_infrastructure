DEVICE_NEXUS_4 = "Nexus 4"
DEVICE_NEXUS_6P = "Nexus 6P"

def getDeviceName(deviceID):
    if (deviceID == "8XV7N16125001298"):
        return "Nexus 6P"
    elif (deviceID == "019602408e90e409"):
        return "Nexus 4"
    else:
        print ("Unknown device ID {}. Please identify your device in DeviceInfo.py.".format(deviceID))
        exit(1)