import json


def is_valid_json(myjson):
    try:
        json_object = json.loads(myjson)
    except ValueError, e:
        print(e)
        return False
    return True