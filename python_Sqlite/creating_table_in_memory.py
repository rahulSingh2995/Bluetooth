#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# We create a friends table in memory. The Id is automatically incremented. 

import sqlite3 as lite

# here the table will be created in memory
# con = lite.connect('test.db')
con = lite.connect(':memory:')

with con:

    cur = con.cursor()

    # In SQLite, INTEGER PRIMARY KEY column is auto incremented starting from 1
    cur.execute("CREATE TABLE friends(id INTEGER PRIMARY KEY, name TEXT);")

    cur.execute("INSERT INTO friends(name) VALUES ('Tom');")
    cur.execute("INSERT INTO friends(name) VALUES ('Rebecca');")
    cur.execute("INSERT INTO friends(name) VALUES ('Jim');")
    cur.execute("INSERT INTO friends(name) VALUES ('Robert');")

    # In SQLite, INTEGER PRIMARY KEY column is auto incremented.
    last_row_id = cur.lastrowid
    print("The last Id of the inserted row is {}".format(last_row_id))
