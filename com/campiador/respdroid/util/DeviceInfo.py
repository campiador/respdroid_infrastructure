import commands

DEVICE_NEXUS_4 = "Nexus 4"
DEVICE_NEXUS_6P = "Nexus 6P"

# This function is no longer used, it's here for backward compatibility
def getDeviceName(deviceID):
    if (deviceID == "8XV7N16125001298"):
        return "Nexus 6P"
    elif (deviceID == "019602408e90e409"):
        return "Nexus 4"
    else:
        print ("Unknown device ID {}. Please identify your device in DeviceInfo.py.".format(deviceID))
        exit(1)

def getDeviceList():
    device_list = []
    ADB_COMMAND_DEVICES = "adb devices"
    (return_value, adb_command_devices_output) = commands.getstatusoutput(ADB_COMMAND_DEVICES)
    if (return_value == 0):
        for line in adb_command_devices_output.splitlines():
            if ("device" in line and "devices" not in line):
                devices = line.split()
                device_list.append(devices[0])
    else:
        print("command {} failed".format(ADB_COMMAND_DEVICES))
        exit(1)
    return device_list