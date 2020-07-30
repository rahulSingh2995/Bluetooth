#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# In this example, we retrieve all data from the cars table. 

import sqlite3 as lite

con = lite.connect('test.db')

with con:

    cur = con.cursor()

    # This SQL statement selects all data from the cars table. 
    cur.execute("SELECT * FROM cars")

    # The fetchall() method gets all records. It returns a result set. Technically, it is a tuple of tuples. Each of the inner tuples represent a row in the table. 
    rows = cur.fetchall()

    for row in rows:
        print(row)

