#!/usr/bin/env python3

import unittest
from adder import object_adder

class TestAdder(unittest.TestCase):
    """A suite to test the adder"""
    
    def test_add_objects_successes(self):
        """Tests suceeding add object tests"""
        object_sum = object_adder(1,2)
        self.assertEqual(3, object_sum, '1 + 2 should be 3')
        
    def test_datatype_errors(self):
        """Tests failing datatype validations"""
        self.assertRaises(TypeError, object_adder, "1",2)
        self.assertRaises(TypeError, object_adder, 1.2,2)
        
if __name__ == '__main__':
    unittest.main()