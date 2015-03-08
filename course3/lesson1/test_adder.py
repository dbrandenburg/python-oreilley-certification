#!/usr/bin/env python3

import unittest
from adder import object_adder
from adder import datatype_errors

class TestAdder(unittest.TestCase):
    """A suite to test the adder"""
    
    def test_add_objects_successes(self):
        """Tests suceeding add object tests"""
        object_sum = object_adder(1,2)
        self.assertEqual(3, object_sum, '1 + 2 should be 3')
        
    def test_datatype_errors(self):
        """Tests failing datatype validations"""
        failing_type_validation_with_string = datatype_errors("1",2)
        failing_type_validation_with_float = datatype_errors(1.2,2)
        self.assertRaises(TypeError, failing_type_validation_with_string)
        self.assertRaises(TypeError, failing_type_validation_with_float)
        
    def test_datatype_successes(self):
        """Tests succeeding datatype validations"""
        succeeding_type_validation = datatype_errors(1,2)
        self.assertIsNone(succeeding_type_validation, "Schould accept two objects of type int")
        
if __name__ == '__main__':
    unittest.main()