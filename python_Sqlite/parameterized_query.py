#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# When we use parameterized queries, we use placeholders instead of directly writing the values into the statements. 
# Parameterized queries increase security and performance.
# The Python sqlite3 module supports two types of placeholders: question marks and named placeholders. 

# We update a price of one car. In this code example, we use the question mark placeholders. 
import sqlite3 as lite

uId = 1
uPrice = 62300

con = lite.connect('test.db')

with con:

    cur = con.cursor()

    # The question marks ? are placeholders for values. The values are added to the placeholders. 
    cur.execute("UPDATE cars SET price=? WHERE id=?", (uPrice, uId))

    # The rowcount property returns the number of updated rows. 
    print("Number of rows updated: {}".format(cur.rowcount))
