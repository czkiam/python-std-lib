#!/usr/bin/env python
"""sample script for namedtuple"""

from collections import namedtuple

ServerAddress = namedtuple('ServerAddress', ['ip_address', 'port'])
LOCAL_WEB_SERVER = ServerAddress('127.0.0.1', 80)
print LOCAL_WEB_SERVER
print LOCAL_WEB_SERVER.ip_address

LOCAL_SSH_SERVER = ServerAddress(port=22, ip_address='127.0.0.1')
print LOCAL_SSH_SERVER.port
print LOCAL_SSH_SERVER[1]

#DIR function
print [m for m in dir(()) if not m.startswith('__')]

print [m for m in dir((ServerAddress)) if not m.startswith('__')]

Novel = namedtuple('Novel', ['title', 'author', 'publication_date'])
pride = Novel('Pride and Prejudice', 'Jane Austen', 1813)

book_title, author, publication_id = pride

print book_title
print author

print pride.publication_date

#cannot re-assign tuple value
#pride.publication_date = 1872

# appropriate way to using tuple
days_of_week = ('Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday')
print days_of_week
