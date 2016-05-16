# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 17:00:31 2016

@author: ksenia
"""
import sqlite3 as lite


db_users = lite.connect("db_users.bd")     
curs = db_users.cursor()
curs.execute("CREATE TABLE users(name TEXT, feat_vect TEXT PRIMARY KEY)")
db_users.commit()
db_users.close()