#!/usr/bin/env python3

"""
Create the food table and add all necessary data.
Note that the foods are identified by the animal's
name and family, so we have to look up the primary key.
"""

import mysql.connector
from database import login_info

db = mysql.connector.Connect(**login_info)
cursor = db.cursor()

cursor.execute("SELECT id FROM animal")
animal_ids = list(*zip(*cursor.fetchall()))
cursor.execute("SELECT anid FROM food")
animal_food_ids = list(*zip(*cursor.fetchall()))

for animal_id in animal_ids:
    if animal_id in animal_food_ids:
        print(animal_id, "OK")
    else:
        print(animal_id, "NOT OK ..exiting")
        exit(0)
