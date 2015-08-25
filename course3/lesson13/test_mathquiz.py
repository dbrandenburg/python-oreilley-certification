#!/usr/bin/env python3
import unittest
import mathquiz

class TestAddresses(unittest.TestCase):
    def test_check_sum(self):
        self.assertEqual("right", mathquiz.check_result('5',2,3), '2 + 3 equals 5')
        self.assertEqual('wrong', mathquiz.check_result('6',2,3), '2 + 3 should not equal 6')

if __name__ == "__main__":
    unittest.main()
