import argparse
import commands
import itertools
from sys import platform

from com.campiador.respdroid.database import DatabaseManager
from com.campiador.respdroid.database.DatabaseManager import load_experiments
from com.campiador.respdroid.graphics import ChartDraw
from com.campiador.respdroid.model.map import DataPreparation
from com.campiador.respdroid.model.map.DataPreparation import deserializeLogcatToRespnodes
from com.campiador.respdroid.storage import PersistentData
from com.campiador.respdroid.storage.PersistentData import atomic_get_new_experiment_number
from com.campiador.respdroid.util import DeviceInfo
from com.campiador.respdroid.util.Config import USE_DUMMY_DATA
from com.campiador.respdroid.util.Log import LOG_VERBOSE, LOG_CLIENT

TAG_RESPDROID_DYNAMIC = "RESPDROID_DYNAMIC"

# CONTROL VARIABLES
# TODO: Eventually there should be no timeout per simulation
LOG_DURATION = 1500 # In seconds
DEFAULT_EXPERIMENT_ID = (259, 269)

NUMBER_OF_ITERATIONS = 10
RUN_ON_CLIENT = False
RECORD_RESULTS = False
DRAW_CHART = True

APP_UNDER_TEST_PACKAGE = "com.campiador.respdroid"


# NOTE: it does not need to be a class
class RespDroid:
    def __init__(self):

        self.devices = DeviceInfo.getDeviceList()

    def check_device_connections(self):
        for device in self.devices:
            print(device)
        if len(self.devices) == 0:
            print("Error: no devices found!")
            exit(1)

    def run_respdroid_dummy_data(self, n_iterations):
        print("running respdroid with dummy data")

        # current_experiment_id = atomic_get_experiment_number()
        # resultLists = get_dummy_data(current_experiment_id)

        load_experiments(0)

        # TODO: do not save dummy data in the future
        # self.store_data(resultLists)

        # ChartDraw.createChart(resultLists, "Responsiveness", "image name and size (KB)", "decode time (ms)")


        # DatabaseManager.print_database()
        # DatabaseManager.load_experiments((66,))

    def runRespDroid(self, n_iterations):
        print ("in runRespDroid")
        self.check_device_connections()

        if RECORD_RESULTS:
            current_experiment_number = atomic_get_new_experiment_number()
        else:
            current_experiment_number = DEFAULT_EXPERIMENT_ID

        # TODO: result lists should be Plotable
        if RUN_ON_CLIENT:
            result_lists_of_n_iterations = self.run_app_record_logcat_and_return_respnode_list(n_iterations,
                                                                                               DEFAULT_EXPERIMENT_ID)
            print "APP RUN FINISHED"

        if LOG_VERBOSE:
            for i, result_list in enumerate(result_lists_of_n_iterations):
                print "result list: ", i
                for result in result_list:
                    print result

        # save results in database?
        if RECORD_RESULTS:
            self.store_data(result_lists_of_n_iterations)

        # Load the same results from database
            # [ img1_i1d1, ,img1i1d2, ...,] nodes with mixed device, iteration, image values
        loaded_result_list = load_experiments(DatabaseManager.QUERY_LIMIT, 259, 269)
        print "loaded results"
        print len(loaded_result_list)
        print loaded_result_list
        # exit(0)

        # [ #d1 [img1_i1, ,img1i2, , ...]
        #  #d2 [img1_i1, ,img1i2], ...] list of nodes, indexed by device type
        device_sublists = DataPreparation.partition_nodelist_by_device_type_return_sublists(loaded_result_list)

        # [#d1 [img1_mean_std, img2_mean_std, img3_mean_std, ...]
        #  #d2 [img1_mean_std, img2_mean_std, img3_mean_std, ...], ...] same as above, but
        # iterations of the same images have been reduced to 1 image
        mean_std_device_sublists = []
        for device_sublist in device_sublists:
            print "\n device sublist:"
            mean_std_device_sublist = DataPreparation.reduce_respnode_n_iterations_to_plotables(device_sublist)
            mean_std_device_sublists.append(mean_std_device_sublist)

        mean_std_device_sublists = DataPreparation.sort_nodelists_by_megapixels(mean_std_device_sublists)
        # print "result_lists:", result_lists
        # print "loaded_result_list:", loaded_result_list

        if DRAW_CHART:
            ChartDraw.plot_with_error_bars(mean_std_device_sublists,
                                           "Responsiveness", "image name and megapixels", "decode time (ms)")
                                           # "Responsiveness", "image name and kilobytes", "decode time (ms)")

        # print_database()
        #
        # exit(0)

    def load_results_for_experiment_4(self):
        nodes_2_n6p_a20 = load_experiments(20, **{DatabaseManager.CL_RESPDROID_DEVICE:
                                                      "\'" + DeviceInfo.DEVICE_NEXUS_6P + "\'",
                                                  DatabaseManager.CL_RESPDROID_IMG_BASE: "\'" + "a.20" + "\'"
                                                  }
                                           )
        nodes_2_n6p_b40 = load_experiments(20, **{DatabaseManager.CL_RESPDROID_DEVICE:
                                                      "\'" + DeviceInfo.DEVICE_NEXUS_6P + "\'",
                                                  DatabaseManager.CL_RESPDROID_IMG_BASE: "\'" + "b.40" + "\'"
                                                  }
                                           )
        nodes_2_n6p_b60 = load_experiments(20, **{DatabaseManager.CL_RESPDROID_DEVICE:
                                                      "\'" + DeviceInfo.DEVICE_NEXUS_6P + "\'",
                                                  DatabaseManager.CL_RESPDROID_IMG_BASE: "\'" + "b.60" + "\'"
                                                  }
                                           )
        nodes_2_n6p_c80 = load_experiments(20, **{DatabaseManager.CL_RESPDROID_DEVICE:
                                                      "\'" + DeviceInfo.DEVICE_NEXUS_6P + "\'",
                                                  DatabaseManager.CL_RESPDROID_IMG_BASE: "\'" + "c.80" + "\'"
                                                  }
                                           )
        nodes_2_n6p_b1100 = load_experiments(20, **{DatabaseManager.CL_RESPDROID_DEVICE:
                                                        "\'" + DeviceInfo.DEVICE_NEXUS_6P + "\'",
                                                    DatabaseManager.CL_RESPDROID_IMG_BASE: "\'" + "b1.100" + "\'"
                                                    }

                                             )
        # N4:
        nodes_2_n4_a20 = load_experiments(20, **{DatabaseManager.CL_RESPDROID_DEVICE:
                                                     "\'" + DeviceInfo.DEVICE_NEXUS_4 + "\'",
                                                 DatabaseManager.CL_RESPDROID_IMG_BASE: "\'" + "a.20" + "\'"
                                                 }
                                          )
        nodes_2_n4_b40 = load_experiments(20, **{DatabaseManager.CL_RESPDROID_DEVICE:
                                                     "\'" + DeviceInfo.DEVICE_NEXUS_4 + "\'",
                                                 DatabaseManager.CL_RESPDROID_IMG_BASE: "\'" + "b.40" + "\'"
                                                 }
                                          )
        nodes_2_n4_b60 = load_experiments(20, **{DatabaseManager.CL_RESPDROID_DEVICE:
                                                     "\'" + DeviceInfo.DEVICE_NEXUS_4 + "\'",
                                                 DatabaseManager.CL_RESPDROID_IMG_BASE: "\'" + "b.60" + "\'"
                                                 }
                                          )
        nodes_2_n4_c80 = load_experiments(20, **{DatabaseManager.CL_RESPDROID_DEVICE:
                                                     "\'" + DeviceInfo.DEVICE_NEXUS_4 + "\'",
                                                 DatabaseManager.CL_RESPDROID_IMG_BASE: "\'" + "c.80" + "\'"
                                                 }
                                          )
        nodes_2_n4_b1_100 = load_experiments(20, **{DatabaseManager.CL_RESPDROID_DEVICE:
                                                        "\'" + DeviceInfo.DEVICE_NEXUS_4 + "\'",
                                                    DatabaseManager.CL_RESPDROID_IMG_BASE: "\'" + "b1.100" + "\'"
                                                    }

                                             )
        n4s = [get_average_in_one_node(nodes_2_n4_b1_100), get_average_in_one_node(nodes_2_n4_b40),
               get_average_in_one_node(nodes_2_n4_c80), get_average_in_one_node(nodes_2_n4_a20),
               get_average_in_one_node(nodes_2_n4_b60)
               ]
        n6ps = [get_average_in_one_node(nodes_2_n6p_b1100),
                get_average_in_one_node(nodes_2_n6p_b40),
                get_average_in_one_node(nodes_2_n6p_c80),
                get_average_in_one_node(nodes_2_n6p_a20),
                get_average_in_one_node(nodes_2_n6p_b60)
                ]
        # only averages count
        nodes = [n4s, n6ps]
        return nodes

    def run_app_record_logcat_and_return_respnode_list(self, n_iterations, current_experiment_id):
        respnode_lists = []

        if LOG_CLIENT:
            print "experiment id: ", current_experiment_id
        iteration = 0
        for _ in itertools.repeat(None, n_iterations):
            iteration += 1
            if LOG_CLIENT:
                print("\nITERATION: {}".format(iteration))
            for device in self.devices:
                # TODO: adbInstall in the future, I will install apps, path to which will be provided through args
                self.adbClearLogcat(device)
                self.adbStopApp(device, APP_UNDER_TEST_PACKAGE)
                self.adbRunApp(device, APP_UNDER_TEST_PACKAGE)
                resultString = self.adbRecordLogcat(device, TAG_RESPDROID_DYNAMIC)
                resultList = deserializeLogcatToRespnodes(resultString, current_experiment_id)
                respnode_lists.append(resultList)

        return respnode_lists

    def store_data(self, resultLists):
        for result_list in resultLists:
            DatabaseManager.insert_objects(result_list)



    # TODO: compile app using gradle wrapper from Android Studio
    def adbCompile(self, app_path):
        adb_command_compile = " /path/to/gradlewrapperinproject/ + gradlew assembleDebug"
        # In a default project setup, the resulting apk can then be found in app/build/outputs/apk/app-debug.apk

    # TODO: install the compiled app
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

    def adbRecordLogcat(self, device, tag):
        print("in adb logcat")
        ADB_COMMAND_LOGCAT = "adb -s " + str(device) + " logcat -s " + tag

        timeout_program_name = self.getOsSpecificTimeout();

        (return_value, adb_command_logcat_output) = \
            commands.getstatusoutput(timeout_program_name + " " + str(LOG_DURATION) + "s " + ADB_COMMAND_LOGCAT)
        print("adb logcat command executed")

        if return_value == 0:
            for line in adb_command_logcat_output.splitlines():
                print line
            else:
                print ("command {} returned with value {}".format(ADB_COMMAND_LOGCAT, return_value))

        return adb_command_logcat_output

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


# Note: Careful here! # TODO: currently have to manually delete
def clear_all_stored_data():
    DatabaseManager.clear_database_if_exists()
    PersistentData.save_experiment_id(0)


def get_average_in_one_node(nodes):
    sum = 0
    for node in nodes:
        sum = sum + int(node.getTimeDuration())
    average= sum / len(nodes)
    nodes[0].delay = str(average)
    return nodes[0]

if __name__ == "__main__":

    DatabaseManager.create_database_if_not_exists()
    if USE_DUMMY_DATA == 1:
        RespDroid().run_respdroid_dummy_data(NUMBER_OF_ITERATIONS)
        # clear_all_stored_data()
        # DatabaseManager.print_database()
    else:
        RespDroid().runRespDroid(NUMBER_OF_ITERATIONS)

