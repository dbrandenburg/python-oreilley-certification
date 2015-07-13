#!/usr/bin/env python3

#class Coconut():
#
#    """A class to provide the weight of a coconut."""
#
#    def __init__(self, coconut_type = None):
#        allowed_coconut_types = {'South Asian': 3,
#                         'Middle Eastern': 2.5,
#                         'American': 3.5}
#        if not coconut_type:
#            for k,v in allowed_coconut_types.items():
#                setattr(self, k, v)
#        elif coconut_type in allowed_coconut_types:
#            setattr(self, 'coconut_type', coconut_type)
#            setattr(self, 'coconut_weight', allowed_coconut_types[coconut_type])
#        else:
#            raise NameError(
#                "API conflict: coconut_type '%s' is not valid" % coconut_type)

class Coconut:
    pass

class SouthAsian(Coconut):
    weight = 3

class MiddleEastern(Coconut):
    weight = 2.5

class American(Coconut):
    weight = 3.5
          
class Inventory():

    """An Inventory class to manage coconuts"""
    def __init__(self):
        self.nuts = [ ]
    
    def add_coconut(self, coconut):
        """Adds a coconut for valid coconut types only"""
        if isinstance(coconut, str):
            raise AttributeError("Coconut must not be string")
        self.nuts.append(coconut)

    def total_weight(self):
        total = 0
        for nut in self.nuts:
            total = total + nut.weight
        return total
        
        
"""Have your Inventory class simply append coconut objects to self.nuts:

class Inventory:

    def __Init__(self):
        self.nuts = [ ]

such that add_coconut appends to self.nuts (nothing more, leave weights out of it completely),
and total_weight simply loops over self.nuts adding the weight attributes of each nut.

Here's a way you might want to organize the Coconut class hierarchy:

class Coconut:
    pass

class SouthAsian(Coconut):
    weight = 3

class MiddleEastern(Coconut):
    weight = 2.5

class American(Coconut):
    weight = 3.5

Then simply going 

nut = American()

gets you a nut of the right weight, ready to add to inventory no problemo.


-Kirby"""