#!/usr/bin/env python3

import unittest
import find_regex

class TestPositionSearch(unittest.TestCase):
    
    def test_sample_text(self):
       self.assertEqual((231,250), find_regex.position_search(), 'Wrong start and end position returned')
    
if __name__ == "__main__":
    unittest.main()