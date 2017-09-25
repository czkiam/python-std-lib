#!/usr/bin/python

from urllib.request import urlopen

url_pluralsight = 'http://pluralsight.com'

method = 'POST'

conn = urlopen(url_pluralsight)

print(type(conn))

#print(dir(conn))

print(conn.url)
print(conn.status)
print(conn.reason)

lines = conn.readlines()
#data = ''.join(lines)

print(lines[0])

data = ''.join(line.decode('utf-8') for line in lines)
print(data)

conn.close()

#http debuging
#https://hookbin.com/

url='https://hookb.in/vyxLVRbA'

method = 'POST'

data = b'{"message":"Hello World!"}'

headers = {'Content-Type': 'application/json'}

import urllib.request as q
httpRequest = q.Request(url, method=method, data=data, headers=headers)

httpConn = urlopen(httpRequest)

responseLines = ''.join([line.decode('utf-8') for line in httpConn.readlines()])

print(responseLines)

httpConn.close()
#r = http.request(method=method, url=url, headers=headers,body=data)

#print(r.read())
