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
        
    def test_retrieve_data_row_objects(self):
        sql = 'SELECT * FROM user WHERE name=\'Steve Holden\';'
        cursor.execute(sql)
        expected_rows = set( )
        for row in cursor.fetchall():
            expected_rows.add(row)

        observed_rows = set( )
        for row in self.c.retrieve(cursor,"name='Steve Holden'"):
            observed_rows.add(row)
            
        print(expected_rows,observed_rows)
        self.assertEqual(observed_rows, expected_rows)


if __name__ == "__main__":
    unittest.main()