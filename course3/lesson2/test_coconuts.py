#!/usr/bin/env python3

import unittest
from coconuts import Coconut
from coconuts import Inventory

class TestCoconuts(unittest.TestCase):
    """A suite to test the Coconut :)"""
    
    def test_different_coconut_weights(self):
        """Tests whether coconuts types have different weights"""
        allowed_coconuts = Coconut()
        weights=allowed_coconuts.__dict__.values()
        self.assertEqual(len(weights),len(set(weights)))
        
    def test_datatype_errors(self):
        """Tests failing datatype validations"""
        inventory = Inventory()
        with self.assertRaises(AttributeError):
            inventory.add_coconut('South Asian')
        
    def test_datatype_successes(self):
        """Tests succeeding datatype validations"""
        inventory = Inventory()
        inventory.add_coconut(Coconut('South Asian'))
        inventory.add_coconut(Coconut('South Asian'))
        inventory.add_coconut(Coconut('Middle Eastern'))
        inventory.add_coconut(Coconut('American'))
        inventory.add_coconut(Coconut('American'))
        inventory.add_coconut(Coconut('American'))
        self.assertEqual(19, inventory.total_weight(), 'Expect total weight to be 19')
        
if __name__ == '__main__':
    unittest.main()