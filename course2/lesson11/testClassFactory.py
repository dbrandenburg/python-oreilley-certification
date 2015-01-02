#!/usr/bin/env python3

import unittest
from classFactory import build_row

import mysql.connector
from database import login_info
db = mysql.connector.Connect(**login_info)
cursor = db.cursor()

class DBTest(unittest.TestCase):
    
    def setUp(self):
        C = build_row("user", "id name email")
        self.c = C([1, "Steve Holden", "steve@holdenweb.com"])

    def test_attributes(self):
        self.assertEqual(self.c.id, 1)
        self.assertEqual(self.c.name, "Steve Holden")
        self.assertEqual(self.c.email, "steve@holdenweb.com")

    def test_repr(self):
        self.assertEqual(repr(self.c),
                         "user_record(1, 'Steve Holden', 'steve@holdenweb.com')")
    
    def test_query(self):
        self.c.retrieve(cursor,condition="WHERE name = 'kerstin'")

if __name__ == "__main__":
    unittest.main()