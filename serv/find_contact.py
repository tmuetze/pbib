#!/usr/bin/env python

from pymongo import MongoClient
import cgi, json, random, requests
print "Content-Type: text/html"
print


fieldStorage = cgi.FieldStorage()
params = {}
for key in fieldStorage.keys():
    params[ key ] = fieldStorage[ key ].value

client = MongoClient()
db = client['pbib']

item = params["item"]
del params["item"]
params["items"] = {"$regex": ".*" + item + ".*"}

users = db.users.find(params)

if users.count() == 0:
    print "<h1> Sorry, there's no one with that item around</h1>"
else:
    try:
        user = users[0]
    except:
        user = users[0]

phone = user["phone"]


colors = ["red", "green", "blue", "yellow"]
color = random.choice(colors)
link = "http://pbib.it/cgi-bin/pbib/serv/color.py?color=" + color
msg = "Someone want's to borrow your %s, please open this link: %s" % (item, link)

nexmo_url = "http://rest.nexmo.com/sms/json?from=pbib&type=text&api_key=0b8382bd&api_secret=7f52886c&to=%(phone)s&text=%(msg)s" % locals()

requests.get(nexmo_url)

print "<meta http-equiv='refresh' content='0; URL=%s'>" % link
