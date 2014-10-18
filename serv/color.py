#!/usr/bin/env python

print "Content-Type: text/html"
print
import cgi
fieldStorage = cgi.FieldStorage()
print "<html>"
print "<body bgcolor='%s'>" % fieldStorage["color"].value
print "<h1>Please wave! ;)</h1>"
print "</body>"
print "</html>"