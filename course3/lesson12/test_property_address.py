#!/usr/bin/env python3
import unittest
from property_address import *

class TestAddresses(unittest.TestCase):

    def setUp(self):
        start_logging(loglevel='INFO')
        self.home = Address( name='Steve Holden', street_address='1972 Flying Circus', city='Arlington', state='VAA', zip_code='12345-1234' )

    def test_name(self):
        self.assertEqual(self.home.name, 'Steve Holden')
        self.assertRaises(AttributeError, setattr, self.home, 'name', 'Daniel Greenfeld')

    def test_state(self):
        self.assertEqual(self.home.state, 'VAA')
        self.assertRaises(StateError, setattr, self.home, 'state', 'Not a state')
        self.home.state = 'COA'
        self.assertEqual(self.home.state, 'COA')

    def test_zip_code(self):
        self.assertEqual(self.home.zip_code, '12345-1234')
        self.assertRaises(ZipCodeError, setattr, self.home, 'zip_code', '123456')
        self.home.zip_code = '12345-1234'
        self.assertEqual(self.home.zip_code, '12345-1234')

if __name__ == "__main__":
    unittest.main()
