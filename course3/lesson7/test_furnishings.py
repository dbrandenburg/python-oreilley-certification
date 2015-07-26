#!/usr/bin/env python3

import unittest
from furnishings import *

class TestFurnishings(unittest.TestCase):
    def test_map_the_home(self):
        home = []
        bed_to_bedroom = Bed('Bedroom')
        sofa_to_livingroom = Sofa('Living Room')
        home.append(bed_to_bedroom)
        home.append(sofa_to_livingroom)
        map_the_home(home)
        self.assertEqual({'Bedroom': bed_to_bedroom, 'Living Room': sofa_to_livingroom}, map_the_home(home), 'message')
        counter(home)
        
if __name__ == "__main__":
    unittest.main()