#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# In this script we connect to the database and fetch the rows of the cars table one by one. 

import sqlite3 as lite

con = lite.connect('test.db')

with con:

    cur = con.cursor()
    cur.execute("SELECT * FROM cars")

    while True:

        # The fetchone() method returns the next row from the table. If there is no more data left, it returns None. 
        row = cur.fetchone()

        if row == None:
            break

        print(row[0], row[1], row[2])

