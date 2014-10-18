#!/usr/bin/env python

from pymongo import MongoClient
import cgi
print "Content-Type: text/html"
print


fieldStorage = cgi.FieldStorage(keep_blank_values=1)
params = {}
for key in fieldStorage.keys():
    params[ key ] = fieldStorage[ key ].value
    if not fieldStorage[ key ].value:
            params[ key ] = ""


client = MongoClient()
db = client['pbib']
db.users.insert(params)

print '{"status":"ok"}'