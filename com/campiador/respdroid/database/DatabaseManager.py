import sqlite3

import MySQLdb
import MySQLdb.cursors
from numpy import size

from com.campiador.respdroid.model.RespNode import RespNode
from com.campiador.respdroid.util.Config import IS_DUMMY



# SCHEMA: id, experiment id, is_dummy? (1=true:0=false), date(time of operation on mobile device),
# device, time (delay-duration of operation), operation, imgbase, imgperc, imgsizeKB
# TODO: think of a primary key

RESPDROID_DB = './database/respdroid.db'
RESPDROID_TB = 'respnodes' # TODO: extract all hardcoded references to this string

CL_RESPDROID_XID = "experiment_id"
CL_RESPDROID_NID = "id"
CL_RESPDROID_IS_DUMMY = "is_dummy"
CL_RESPDROID_DATETIME = "date"
CL_RESPDROID_DEVICE = "device"
CL_RESPDROID_DELAY = "time"
CL_RESPDROID_OPERATION = "operation"
CL_RESPDROID_IMG_BASE = "imgbase"
CL_RESPDROID_IMG_PERC = "imgperc"
CL_RESPDROID_IMG_SIZE_KB = "imgsizekb"

def create_database_if_not_exists():
    global c, conn
    conn = sqlite3.connect(RESPDROID_DB)
    c = conn.cursor()

    if not table_exists(c):
        print "table does not exist"
        c.execute('''CREATE TABLE respnodes ({id} integer primary key, {xid} integer, {isdummy} integer, {date} text, 
                 {device} text, {time} text, {operation} text, {imgbase} text, {imgperc} integer, {imgsizekb} integer)'''
                  .format(id=CL_RESPDROID_NID, xid=CL_RESPDROID_XID, isdummy = CL_RESPDROID_IS_DUMMY,
                          date=CL_RESPDROID_DATETIME, device=CL_RESPDROID_DEVICE, time=CL_RESPDROID_DELAY,
                          operation=CL_RESPDROID_OPERATION, imgbase=CL_RESPDROID_IMG_BASE, imgperc=CL_RESPDROID_IMG_PERC,
                          imgsizekb=CL_RESPDROID_IMG_SIZE_KB))
    # Save (commit) the changes
    conn.commit()
    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    conn.close()

# FIXME: respdroid constructor contract has been updated
def insert_test_data():
    respnodes = [RespNode("Nexus Dummy", 420, "decode-image", "sample_img_4", 1, 1300),
                 RespNode("Nexus Dummy", 320, "decode-image", "sample_img_3", 1, 1200)]
    insert_objects(respnodes)


def table_exists(c):
    t = ('table', 'respnodes',)
    c.execute('SELECT name FROM sqlite_master WHERE type=? AND name=?', t)

    if c.fetchone():
        return True
    else:
        return False


def insert_query(data):
    global c, conn
    conn = sqlite3.connect(RESPDROID_DB)
    c = conn.cursor()
    # NOTE: using a NULL to have SQLite insert an auto-generated id
    c.executemany('INSERT INTO respnodes VALUES (NULL,?,?,?,?,?,?,?,?,?)', data)
    conn.commit()
    conn.close()


def print_database():
    print "printintg database content"
    # this variable holds the true, we use the tuple to prevent sql injection attacks
    global c, conn
    conn = sqlite3.connect(RESPDROID_DB)
    c = conn.cursor()

    t = (1,)
    c.execute('SELECT * FROM respnodes WHERE isdummy=?', t)
    data = (c.fetchall())

    for item in data:
        print item


def insert_objects(respnodes):
    query_data = map_objects_to_relational(respnodes)
    insert_query(query_data)


def map_objects_to_relational(respnodes):
    query_data= []
    for respnode in respnodes:
        # TODO: timestamp should be handled in a higher level
        query_data.append((respnode.getExperimentId(), IS_DUMMY, respnode.get_timestamp(),
                           respnode.getDevice(), respnode.getTimeDuration(), respnode.getOperation(),
                           respnode.getBaseParam(), respnode.getScaleParam(), respnode.getImgSize()))
    return query_data


# TODO: map relational to objects
def map_relational_to_objects(data_list):
    """TODO: this is needed for creating chart from past experiments"""


def clear_database_if_exists():
    """TODO: clear table and database"""
    global c, conn
    conn = sqlite3.connect(RESPDROID_DB)
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS respdroid.respnodes")
    conn.commit()
    conn.close()


def load_experiments(experiments_tuple):
    print "loading experiments"
    condition = " WHERE"

    for index, experiment in enumerate(experiments_tuple):
        if index == 0:
            condition = condition + " " + CL_RESPDROID_XID + " = " + "?"
        else:
            condition = condition + " OR " + CL_RESPDROID_XID + " = " + "?"

    global conn, c
    conn = sqlite3.connect(RESPDROID_DB)
    conn.text_factory = str
    conn.row_factory = sqlite3.Row
    c = conn.cursor()

    query = "SELECT * FROM " + RESPDROID_TB + condition
    c.execute(query, experiments_tuple)
    data = (c.fetchall())

    object_node_list = []

    for experiment in data:
            object_node = RespNode(experiment[CL_RESPDROID_NID], experiment[CL_RESPDROID_XID],
                                   experiment[CL_RESPDROID_DELAY], experiment[CL_RESPDROID_DEVICE],
                                   experiment[CL_RESPDROID_DELAY], experiment[CL_RESPDROID_OPERATION],
                                   experiment[CL_RESPDROID_IMG_BASE], experiment[CL_RESPDROID_IMG_PERC],
                                   experiment[CL_RESPDROID_IMG_SIZE_KB]
                                   )
            object_node_list.append(object_node)

    return object_node_list

def load_objects():
    print "loading objects"
    # this variable holds the true, we use the tuple to prevent sql injection attacks
    global c, conn
    conn = sqlite3.connect(RESPDROID_DB)
    c = conn.cursor()

    t = (1,)
    c.execute('SELECT * FROM respnodes WHERE isdummy=?', t)
    data = (c.fetchall())

    for item in data:
        print item