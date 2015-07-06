#!/usr/bin/env python3

class Coconut():

    """A class to provide the weight of a coconut."""

    def __init__(self, coconut_type = None):
        allowed_coconut_types = {'South Asian': 3,
                         'Middle Eastern': 2.5,
                         'American': 3.5}
        if not coconut_type:
            for k,v in allowed_coconut_types.items():
                setattr(self, k, v)
        elif coconut_type in allowed_coconut_types:
            setattr(self, 'coconut_type', coconut_type)
            setattr(self, 'coconut_weight', allowed_coconut_types[coconut_type])
        else:
            raise NameError(
                "API conflict: coconut_type '%s' is not valid" % coconut_type)

            
class Inventory():

    """An Inventory class to manage coconuts"""

    def add_coconut(self, coconut):
        "Adds a coconut for valid coconut types only"
        if isinstance(coconut, str):
            raise AttributeError("Coconut must not be string")
        if hasattr(self, 'Total'):
            total_weight = self.__dict__['Total'] + coconut.coconut_weight
            setattr(self, 'Total', total_weight)
        else:
            setattr(self, 'Total', coconut.coconut_weight)

    def total_weight(self):
        return self.__dict__['Total']