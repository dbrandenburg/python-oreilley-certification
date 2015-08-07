#!/usr/bin/env python3

import unittest
from furnishings import *

class TestFurnishings(unittest.TestCase):
            
    def test_map(self):
        self.home = []
        self.home.append(Bed('Bedroom'))
        self.home.append(Sofa('Living Room'))
        self.home.append(Table('Bedroom'))

        mapping = map_the_home(self.home)
        self.assertTrue(isinstance(mapping['Bedroom'][0], Bed))
        self.assertTrue(isinstance(mapping['Living Room'][0], Sofa))
        self.assertTrue(isinstance(mapping['Bedroom'][1], Table))        
        
if __name__ == "__main__":
    unittest.main()