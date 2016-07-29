import json

class MySerializer(object):

    @classmethod
    def deserialize(cls,jsonstr):
        #load from json to dict
        #initialize object, return
        json_data = json.loads(jsonstr)
        return cls(json_data)

    def serialize(self):
        #iterate over self.my_attrs
        pass
        #get attrs, set into dictionary
        #return dumps(dictionary)
