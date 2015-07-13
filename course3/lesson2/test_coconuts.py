#!/usr/bin/env python3

import unittest
from coconuts import SouthAsian, MiddleEastern, American
from coconuts import Inventory

class TestCoconuts(unittest.TestCase):
    """A suite to test the Coconut :)"""
    
    def test_different_coconut_weights(self):
        """Tests whether coconuts types have different weights"""
        inventory = Inventory()
        inventory.add_coconut(SouthAsian())
        inventory.add_coconut(MiddleEastern())
        inventory.add_coconut(American())
        weights=[nut.weight for nut in inventory.nuts]
        self.assertEqual(len(weights),len(set(weights)))
        
    def test_datatype_errors(self):
        """Tests failing datatype validations"""
        inventory = Inventory()
        with self.assertRaises(AttributeError):
            inventory.add_coconut('SouthAsian')
        
    def test_datatype_successes(self):
        """Tests succeeding datatype validations"""
        inventory = Inventory()
        inventory.add_coconut(SouthAsian())
        inventory.add_coconut(SouthAsian())
        inventory.add_coconut(MiddleEastern())
        inventory.add_coconut(American())
        inventory.add_coconut(American())
        inventory.add_coconut(American())
        self.assertEqual(19, inventory.total_weight(), 'Expect total weight to be 19')
        
if __name__ == '__main__':
    unittest.main()