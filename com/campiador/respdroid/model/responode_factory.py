import simplejson

from com.campiador.respdroid.model.RespNode import RespNode


# Deserialize
def deserialize_json_to_respnode(s):
    clones = simplejson.loads(s)
    print clones
    # # Now give our clones some life
    # for clone in clones:
    #     respNode = RespNode()
    #     respNode.__dict__ = clone
    #     print respNode
    # return respNode


# TODO: more polymorphic code: deserialize without reading the dictionary key stings
def deserialize_dict_to_respnode(dct):
    return RespNode(dct['node_id'], dct['experiment_id'], dct['timestamp'], dct['device'], dct['delay'],
                    dct['operation'], dct['img_base'], dct['img_perc'], dct['img_sizeKB'], dct['imgWidth'],
                    dct['imgHeight'], dct['os_version_release_name'], dct['package_name'], dct['app_name'],
                    dct['app_version_code'], dct['activity_name'])
