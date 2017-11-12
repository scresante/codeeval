#!/usr/bin/python3
from sys import argv
try:
  FILE = argv[1]
except NameError:
  FILE = 'tests/225'
DATA = open(FILE, 'r').read().splitlines()

for line in DATA:
    if not line:
        continue
    q,w = line.split(' | ')
    errnum = len([ (A,B) for (A,B) in zip(q,w) if A!=B ])
    if errnum > 6:
        print('Critical')
    elif errnum > 4:
        print('High')
    elif errnum > 2:
        print('Medium')
    elif errnum > 0:
        print('Low')
    else:
        print('Done')

