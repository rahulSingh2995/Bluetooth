#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# In this section, we are going to insert an image to the SQLite database. 
# Note that some people argue against putting images into databases. 

"""sqlite> CREATE TABLE images(id INTEGER PRIMARY KEY, data BLOB);

For this example, we create a new table called Images. For the images, we use the BLOB data type, which stands for Binary Large Objects."""

import sqlite3 as lite
import sys

def readImage():

    fin = None

    try:
        fin = open("ganesh.jpg", "rb")
        img = fin.read()
        return img

    except IOError as e:

        print(e)
        sys.exit(1)

    finally:

        if fin:
            fin.close()


try:
    con = lite.connect('test.db')

    cur = con.cursor()

    data = readImage()
    binary = lite.Binary(data)
    cur.execute("INSERT INTO images(data) VALUES (?)", (binary,) )

    con.commit()

except lite.Error as e:

    if con:
        con.rollback()

    print(e)
    sys.exit(1)

finally:

    if con:
        con.close()

