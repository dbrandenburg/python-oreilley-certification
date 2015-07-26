#!/usr/bin/env python3

class Furnishings:
    def __init__(self,room):
        self.room = room
        
class Sofa(Furnishings):
    pass
    
class Bookshelf(Furnishings):
    pass
    
class Bed(Furnishings):
    pass

class Table(Furnishings):
    pass
        

def map_the_home(home):
    home_map = {}
    for furniture in home:
        home_map.update({furniture.__dict__['room']:furniture})
    return home_map

def counter(home):
    for furnish in Furnishings.__subclasses__():
        furnish_name = furnish.__name__
        furnish_name_count = 0
        for furniture in home:
            if furniture.__class__.__name__ == furnish_name:
                furnish_name_count += 1
        print(furnish_name + ':', furnish_name_count)
        
        
bla = Furnishings('s')