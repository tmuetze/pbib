#!/usr/bin/env python

from pymongo import MongoClient
import cgi
import random
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

params["items"] = ""
for (k, v) in params.items():
    if v == "on":
        params["items"] += k + ","
        del params[k]

db.users.insert(params)
# link = "http://localhost:8080/search.html"
link = "http://pbib.it/pbib/search.html"
print "<meta http-equiv='refresh' content='0; URL=%s'>" % link
