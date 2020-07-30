#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# The default cursor returns the data in a tuple of tuples. When we use a dictionary cursor, the data is sent in the form of Python dictionaries. 
# This way we can refer to the data by their column names. 
# In this example, we print the contents of the cars table using the dictionary cursor. 

import sqlite3 as lite

con = lite.connect('test.db')

with con:

    # We select a dictionary cursor. Now we can access records by the names of columns. 
    con.row_factory = lite.Row

    cur = con.cursor()
    cur.execute("SELECT * FROM cars")

    rows = cur.fetchall()

    for row in rows:
        print("{} {} {}".format(row["id"], row["name"], row["price"]))
