#!/usr/bin/env python3
import unittest
from sstr import Sstr


class SstringTestCases(unittest.TestCase):
    def test_shifting(self):
        s1 = Sstr("abcde")
        self.assertEqual('abcde', s1 << 0, 'Lshift 0')
        self.assertEqual('abcde', s1 >> 0, 'Rshift 0')
        self.assertEqual('cdeab', s1 << 2, 'Lshift 2')
        self.assertEqual('deabc', s1 >> 2, 'Rshift 2')
        self.assertEqual('abcde', s1 >> 5, 'Rshift 5')
        self.assertEqual('abcde', (s1 >> 5) << 5, 'Rshift / Lshift 5')

if __name__ == "__main__":
    unittest.main()
