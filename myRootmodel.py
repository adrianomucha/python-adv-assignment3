from assignment import MySerializer

class Mymodel(MySerializer):
    my_attrs = ('an_attr', 'another_attr')

    def __init__(self, kwargs):
        for i  in self.my_attrs:


            setattr(self, i, kwargs.get(i))


my_thing(an_attr=1, another_attr=100, another_second_attr= 200)
