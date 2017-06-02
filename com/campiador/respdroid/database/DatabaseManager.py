import sqlite3

from com.campiador.respdroid.model.RespNode import RespNode


# SCHEMA: is_dummy? (1=true:0=false), date(time of transaction),
# device, time (delay), operation, imgbase, imgperc, imgsizeKB
# TODO: think of a primary key
RESPDROID_DB = './database/respdroid.db'


def create_database_if_not_exists():
    global c, conn
    conn = sqlite3.connect(RESPDROID_DB)
    c = conn.cursor()

    if table_exists(c):
        print "table exists"
    else:
        print "table does not exist"
        # Create table TODO: add timestamp, primary key for event id, and unique group id
        c.execute('''CREATE TABLE respnodes 
                 (isdummy integer, date text, 
                 device text, time text, operation text, imgbase text, imgperc integer, imgsizekb integer)''')
    # Save (commit) the changes
    conn.commit()
    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    conn.close()


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
    c.executemany('INSERT INTO respnodes VALUES (?,?,?,?,?,?,?,?)', data)
    conn.commit()
    conn.close()


def read_database():
    # this variable holds the true, we use the tuple to prevent sql injection attacks
    global c, conn
    conn = sqlite3.connect(RESPDROID_DB)
    c = conn.cursor()

    t = (1,)
    c.execute('SELECT * FROM respnodes WHERE isdummy=?', t)
    data = (c.fetchall())


def insert_objects(respnodes):
    query_data = convert_objects_to_query(respnodes)
    insert_query(query_data)


def convert_objects_to_query(respnodes):
    query_data= []
    for respnode in respnodes:
        # TODO: timestamp and dummy flag should be handled in a higher level
        query_data.append((1, '2017-05-30', respnode.getDevice(), respnode.getTimeDuration(), respnode.getOperation(),
                           respnode.getBaseParam(), respnode.getScaleParam(), respnode.getImgSize()))
    return query_data


def clear_database():
    "TODO: clear table and database"


create_database_if_not_exists()
# read_database()