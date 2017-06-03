import sqlite3

from com.campiador.respdroid.model.RespNode import RespNode
from com.campiador.respdroid.util.Config import IS_DUMMY


# SCHEMA: id, experiment id, is_dummy? (1=true:0=false), date(time of operation on mobile device),
# device, time (delay-duration of operation), operation, imgbase, imgperc, imgsizeKB
# TODO: think of a primary key

RESPDROID_DB = './database/respdroid.db'
RESPDROID_TB = 'respnodes' # TODO: extract all hardcoded references to this string


def create_database_if_not_exists():
    global c, conn
    conn = sqlite3.connect(RESPDROID_DB)
    c = conn.cursor()

    if not table_exists(c):
        print "table does not exist"
        c.execute('''CREATE TABLE respnodes (id integer primary key, experiment_id integer,  
                 isdummy integer, date text, 
                 device text, time text, operation text, imgbase text, imgperc integer, imgsizekb integer)''')
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
