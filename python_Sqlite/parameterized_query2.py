#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# The second example uses parameterized statements with named placeholders. 
# We select a name and a price of a car using named placeholders. 

import sqlite3 as lite

uId = 4

con = lite.connect('test.db')

with con:

    cur = con.cursor()

    # The named placeholders start with a colon character. 
    cur.execute("SELECT name, price FROM cars WHERE Id=:Id", {"Id": uId})

    row = cur.fetchone()
    print row[0], row[1]
