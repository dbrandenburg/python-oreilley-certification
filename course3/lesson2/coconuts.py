#!/usr/bin/env python3

class Bunch(object):
    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                raise AttributeError("API conflict: '%s' is part of the '%s' API" % (key, self.__class__.__name__))
            else:
                setattr(self, key, value)
    def pretty(self):
        text = ""
        for key, value in self.__dict__.items():
            text += "%s: %s\n" % (key, value)
        return text
        
class Inventory(Bunch):
    def add_coconut(self, coconut_type):
        """Adds a coconut for valid coconut types only"""
        coconut_types = { 
            'South Asian': 3,
            'Middle Eastern': 2.5,
            'American': 3.5 }
        
        if coconut_type not in coconut_types:
            raise KeyError("Coconut Type '%s' not supported." % (self.coconut_type))

        else:
            weight = coconut_types[coconut_type]
            setattr(self, coconut_type, weight)
            if hasattr(self, 'Total'):
                total_weight = self.__dict__['Total'] + weight
                setattr(self, 'Total', total_weight)
            else:
                setattr(self, 'Total', weight)
    
    def total_weight(self):
self.__dict__['Total']

inventory = Inventory()
inventory.add_coconut('South Asian')
inventory.add_coconut('South Asian')
inventory.add_coconut('Middle Eastern')
print(inventory.total_weight())

    #total_weight():
