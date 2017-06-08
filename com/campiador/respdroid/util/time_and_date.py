# for keeping track of experiment timestamp

import time

import datetime

# TODO: timeinmillies?
def get_current_timestamp():
    ts = time.time()
    stamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    return stamp


