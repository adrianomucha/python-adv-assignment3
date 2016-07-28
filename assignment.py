import json

class MySerializer(object):

    @classmethod
    def deserialize(cls,jsonstr):
        #load from json to dict
        #initialize object, return
        json_data = json.loads(jsonstr)
        json.loads(jsonstr) = cls
        return cls(**d)

    def serialize(self):
        #iterate over self.my_attrs

        #get attrs, set into dictionary
        #return dumps(dictionary)
        with open jsonstr
