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
        #print(row[0],row[2])

    altered_car = []
    cur.execute("SELECT * FROM cars")
    for i in range(len(rows)):
        row = cur.fetchone()
        altered_car.append((row[0],row[2]))

    #print(altered_car)

    altered_car = tuple(altered_car)
    print(type(altered_car))
    cur2 = con.cursor()
    
    cur2.execute("CREATE TABLE IF NOT EXISTS altered_cars (id INT, price INT)")
    cur2.executemany("INSERT INTO altered_cars VALUES(?, ?)",altered_car)

    cur2.execute("SELECT * FROM altered_cars")
    rows = cur2.fetchall()

    #for row in rows:
    print(rows)
