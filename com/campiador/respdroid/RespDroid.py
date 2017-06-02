import argparse
import commands
from sys import platform

from com.campiador.respdroid.database import DatabaseManager
from com.campiador.respdroid.graphics import ChartTest
from com.campiador.respdroid.graphics.ChartDrawer import ChartDrawer
from com.campiador.respdroid.util import DeviceInfo
from com.campiador.respdroid.util.DataPreparation import DataPreparation
from com.campiador.respdroid.model.RespNode import RespNode

LOG_TIME = 10
NUMBER_OF_REPETITIONS = 10





class RespDroid:
    def __init__(self):
        self.APP_PACKAGE = "com.campiador.respdroid"
        self.TAG_RESPDROID_DYNAMIC = "RESPDROID_DYNAMIC"
        self.devices = self.getDeviceList()

    def check_device_connections(self):
        for device in self.devices:
            print(device)
        if len(self.devices) == 0:
            print("Error: no devices found!")
            exit(1)

    def run_respdroid_dummy_data(self, repeat_count):
        print("running respdroid with dummy data")
        resultLists = self.get_dummy_data()

        self.store_data(resultLists)  # continue here: database does not work

        ChartTest.createChart(resultLists, "Responsiveness", "image name and size (KB)", "decode time (ms)")

        DatabaseManager.read_database()


    def runRespDroid(self, repetition_max):
        print ("in runRespDroid")
        self.check_device_connections()

        resultLists = []  # this list will be filled by logcat
        resultLists = self.logcat_to_respnode_list(resultLists)

        ChartTest.createChart(resultLists, "Responsiveness", "image name and size (KB)", "decode time (ms)")



    def logcat_to_respnode_list(self, resultLists):
        for device in self.devices:
            # adbInstall in the future, I will install apps, path to which will be provided through args
            self.adbClearLogcat(device)
            self.adbStopApp(device, self.APP_PACKAGE)
            self.adbRunApp(device, self.APP_PACKAGE)
            resultString = self.adbLogcat(device, self.TAG_RESPDROID_DYNAMIC)
            resultLists.append(DataPreparation().convertStringToImageList(resultString))
        return resultLists

    def getDeviceList(self):
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


    def store_data(self, resultLists):
        for result_list in resultLists:
            DatabaseManager.insert_objects(result_list)

    def get_dummy_data(self):
        resultLists = [
            [
                RespNode("Nexus 4", 60, "decode-image", "sample_img_0", 1, 900),
                RespNode("Nexus 4", 120, "decode-image", "sample_img_1", 1, 1000),
                RespNode("Nexus 4", 220, "decode-image", "sample_img_2", 1, 1100),
                RespNode("Nexus 4", 320, "decode-image", "sample_img_3", 1, 1200),
                RespNode("Nexus 4", 420, "decode-image", "sample_img_4", 1, 1300),
            ]
            ,
            [
                RespNode("Nexus 6", 40, "decode-image", "sample_img_0", 1, 900),
                RespNode("Nexus 6", 80, "decode-image", "sample_img_1", 1, 1000),
                RespNode("Nexus 6", 180, "decode-image", "sample_img_2", 1, 1100),
                RespNode("Nexus 6", 280, "decode-image", "sample_img_3", 1, 1200),
                RespNode("Nexus 6", 380, "decode-image", "sample_img_4", 1, 1300)
            ]
        ]
        return resultLists

    # TODO: compile app using gradle wrapper from Android Studio
    def adbCompile(self, app_path):
        adb_command_compile = " /path/to/gradlewrapperinproject/ + gradlew assembleDebug"
        # In a default project setup, the resulting apk can then be found in app/build/outputs/apk/app-debug.apk

    def adbInstall(self, device, app_path):
        ADB_COMMAND_INSTALL = "adb -s " + device + " install" + app_path

    def adbRunApp(self, device, appPackage):
        ADB_COMMAND_RUN = "adb -s " + str(device) + " shell monkey -p " + str(appPackage) + " 1"
        (return_value, adb_command_run_output) = commands.getstatusoutput(ADB_COMMAND_RUN)
        if (return_value == 0):
            print(adb_command_run_output)
        else:
            print("command {} failed".format(ADB_COMMAND_RUN))
            exit(1)

    def adbStopApp(self, device, appPackage):
        adb_command_stop = "adb -s " + str(device) + " shell am force-stop " + appPackage
        (return_value, adb_command_stop_output) = commands.getstatusoutput(adb_command_stop)
        if (return_value == 0):
            print (adb_command_stop_output)
        else:
            print("command {} failed".format(adb_command_stop))
            exit(1)

    def adbClearLogcat(self, device):
        adb_command_clear_logcat = "adb -s " + str(device) + " logcat -c"
        (return_value, adb_command_logcat_clear_output) = commands.getstatusoutput(adb_command_clear_logcat)
        if return_value == 0:
            for line in adb_command_logcat_clear_output.splitlines():
                print line
            else:
                print ("command {} had return value {}".format(adb_command_clear_logcat, return_value))

    def adbLogcat(self, device, tag):
        print("in adb logcat")
        ADB_COMMAND_LOGCAT = "adb -s " + str(device) + " logcat -s " + tag

        timeout_program_name = self.getOsSpecificTimeout();

        (return_value, adb_command_logcat_output) = \
            commands.getstatusoutput(timeout_program_name + " " + str(LOG_TIME) + "s " + ADB_COMMAND_LOGCAT)
        print("adb logcat command executed")

        if (return_value == 0):
            for line in adb_command_logcat_output.splitlines():
                print line
            else:
                print ("command {} returned with value {}".format(ADB_COMMAND_LOGCAT, return_value))

        return adb_command_logcat_output

    # NOTE:Function polymorphism does not exist in python, the last function will be used.
    # def adbLogcat(self, tag):
    #     print("in adb logcat")
    #
    #     ADB_COMMAND_LOGCAT = "adb logcat -s " + tag
    #     (return_value, adb_command_logcat_output) = \
    #         commands.getstatusoutput("timeout " + str(LOG_TIME)+ "s " + ADB_COMMAND_LOGCAT)
    #     print("adb logcat command executed")
    #     print("return_value:" + str(return_value))
    #
    #     for line in adb_command_logcat_output.splitlines():
    #         print line
    #
    #     if (return_value == 0):
    #         for line in adb_command_logcat_output.splitlines():
    #             print line
    #     else:
    #         print ("command {} returned with value {}".format(ADB_COMMAND_LOGCAT, return_value))
    #
    #     return adb_command_logcat_output


    #     TODO: process args, e.g. app path
    def parseArgs(self):
        parser = argparse.ArgumentParser(description='Process some integers.')
        parser.add_argument('integers', metavar='N', type=int, nargs='+',
                            help='an integer for the accumulator')
        parser.add_argument('--app', dest='accumulate', action='store_const',
                            const=sum, default=max,
                            help='app path (default: not defined)')

        args = parser.parse_args()
        print args.accumulate(args.integers)

    #TODO: check to see if timeout is installed at all
    def getOsSpecificTimeout(self):
        if platform == "linux" or platform == "linux2":
            # linux
            return "timeout"
        elif platform == "darwin":
            # OS X
            return "gtimeout"
        else:  # platform == "win32":
            # Windows...
            return "timeout"


# RespDroid().runRespDroid(NUMBER_OF_REPETITIONS)
RespDroid().run_respdroid_dummy_data(NUMBER_OF_REPETITIONS)
