import json

class MySerializer(object):

    @classmethod
    def deserialize(cls,jsonstr):
        #load from json to dict
        #initialize object, return
        json_data = json.loads(jsonstr)
        return cls(json_data)

    def serialize(self):
        #need to convert: from dict to json
        #refer ti the dict: use json.dump to transfer
        #dict to string
        #iterate over self.my_attrs
        pass
        #get attrs, set into dictionary
        #return dumps(dictionary)
