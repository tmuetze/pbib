#!/usr/bin/env python

from pymongo import MongoClient
import cgi, json
print "Content-Type: text/html"
print


fieldStorage = cgi.FieldStorage()
params = {}
for key in fieldStorage.keys():
    params[ key ] = fieldStorage[ key ].value

client = MongoClient()
db = client['pbib']
users = db.users.find()

items = []

for user in users:
    if "items" in user:
        c_items = user["items"].split(",")
        for c_item in c_items:
            if c_item not in items:
                items.append(c_item)

print json.dumps(items)
