from com.campiador.respdroid.RespDroid import get_average_in_one_node
from com.campiador.respdroid.database import DatabaseManager
from com.campiador.respdroid.database.DatabaseManager import load_experiments
from com.campiador.respdroid.graphics import ChartDraw
from com.campiador.respdroid.util import DeviceInfo


def experiment_1():
    pass
    # # XP1:
    nodes_1 = load_experiments(10, **{DatabaseManager.CL_RESPDROID_DEVICE:
                                          "\'" + DeviceInfo.DEVICE_NEXUS_6P + "\'",
                                      DatabaseManager.CL_RESPDROID_IMG_BASE: "\'" + "b.20" + "\'"
                                      }

                               )

    ChartDraw.create_box_chart_x1(nodes_1, "Respdroid Statistics", "size in KB", "operation delay")


def experiment_2():
    pass
    # XP 2:
    nodes_2_n6p = load_experiments(100, **{DatabaseManager.CL_RESPDROID_DEVICE:
                                               "\'" + DeviceInfo.DEVICE_NEXUS_6P + "\'",
                                           DatabaseManager.CL_RESPDROID_IMG_BASE: "\'" + "a.20" + "\'"
                                           }

                                   )

    nodes_2_n4 = load_experiments(100, **{DatabaseManager.CL_RESPDROID_DEVICE:
                                              "\'" + DeviceInfo.DEVICE_NEXUS_4 + "\'",
                                          DatabaseManager.CL_RESPDROID_IMG_BASE: "\'" + "a.20" + "\'"
                                          }

                                  )

    sum_2_n4 = 0
    for node in nodes_2_n4:
        sum_2_n4 = sum_2_n4 + int(node.getTimeDuration())
    average_2_n4 = sum_2_n4 / len(nodes_2_n4)
    nodes_2_n4[0].delay = str(average_2_n4)

    sum_2_n6p = 0
    for node in nodes_2_n6p:
        sum_2_n6p = sum_2_n6p + int(node.getTimeDuration())
    average_2_n6p = sum_2_n6p / len(nodes_2_n6p)
    nodes_2_n6p[0].delay = str(average_2_n6p)

    # only averages count
    nodes = [[nodes_2_n4[0]], [nodes_2_n6p[0]]]
    ChartDraw.createChart(nodes, "Responsiveness", "image name and size (KB)", "decode time (ms)")


def experiment3():
    # pass
    #
    # # XP 3:
    # #N6
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
    ChartDraw.createChart(nodes, "Responsiveness", "image name and size (KB)", "decode time (ms)")

    # ChartDraw.create_box_chart_x1(nodes_1, "Respdroid Statistics", "size in KB", "operation delay")


def experiment_4():
    # XP 4:
    # N6
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
    ChartDraw.x4_createChart(nodes, "Responsiveness", "image name and megapixels", "decode time (ms)")