#!/usr/bin/env python3
import unittest

class SubDict(dict):
    def __init__(self, default):
        dict.__init__(self)
        self.default = default

    def __getitem__(self, key):
        try:
            return dict.__getitem__(self, key)
        except KeyError:
            return self.default

class SubDictTest(unittest.TestCase):
    def test_sub_dict(self):
        sd = SubDict('default_value')
        sd['key01'] = 'value01'
        sd['key02'] = 'value01'
        self.assertEqual({'key01': 'value01', 'key02': 'value01'}, sd,
                          'Should contain set keys and values.')
        self.assertEqual('default_value', sd['not_existent'],
                              'Should return default value.')

if __name__ == "__main__":
    unittest.main()
