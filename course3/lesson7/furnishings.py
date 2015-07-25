#!/usr/bin/env python3

class Furnishing:
    def __init__(self,room):
        self.room = room
    
class Sofa(Furnishing):
    pass
    
class Bookshelf(Furnishing):
    pass
    
class Bed(Furnishing):
    pass

class Table(Furnishing):
    pass
        
home = []
home.append(Bed('Bedroom'))
home.append(Sofa('Living Room'))
print(home)

#def map_the_home(home):
    