#!/usr/bin/python3
from sys import argv
try:
  f = argv[1]
except:
  f = 'tests/174'
data = open(f,'r').read().splitlines()

import itertools
add = [', yeah!',', this is crazy, I tell ya.',', can U believe this?',', eh?',', aw yea.',', yo.','? No way!','. Awesome!']


countpunk = 0
for line in data:
    if not line:
        continue
    for char in line:
        if ( char == '.' or char =='?' or char == '!'):
            countpunk += 1
print(countpunk)
