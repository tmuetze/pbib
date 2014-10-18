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

print "["
# print "records with following filter:" + str(params)
print
item = params["item"]
del params["item"]
params["items"] = {"$regex": ".*" + item + ".*"}

results = db.users.find(params)

for result in results:
    result["_id"] = str(result["_id"])  #
    result["item"] = item
    print json.dumps(dict(result), indent=4)
    print ", "
print "]"
