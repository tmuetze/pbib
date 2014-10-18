#!/usr/bin/env python

print "Content-Type: text/html"
print

from bson.objectid import ObjectId
import cgi, random
from pymongo import MongoClient

fieldStorage = cgi.FieldStorage()
id = fieldStorage["_id"].value
item = fieldStorage["item"].value

client = MongoClient()
db = client['pbib']

user = db.users.find({"_id":ObjectId(id)})[0]
phone = user["phone"]


colors = ["red", "green", "blue", "yellow"]
color = random.choice(colors)
link = "http://pbib.it/cgi-bin/pbib/serv/color.py?color=" + color
msg = "Someone want's to borrow your %s, please open this link: %s" % (item, link)

url = "http://rest.nexmo.com/sms/json?from=pbib&type=text&api_key=0b8382bd&api_secret=7f52886c&to=%(phone)s&text=%(msg)s" % locals()
print url
user = db.users.find({"_id":ObjectId(id)})[0]
