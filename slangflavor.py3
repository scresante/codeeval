#!/usr/bin/python3
from sys import argv
try:
  FILE = argv[1]
except NameError:
  FILE = 'tests/174'
DATA = open(FILE, 'r').read().splitlines()

import itertools
add = [', yeah!',', this is crazy, I tell ya.',', can U believe this?',', eh?',', aw yea.',', yo.','? No way!','. Awesome!']


countpunk = 0
for line in DATA:
    if not line:
        continue
    for char in line:
        if ( char == '.' or char =='?' or char == '!'):
            countpunk += 1
print(countpunk)
