#!/usr/bin/python3
from sys import argv
try:
  f = argv[1]
except:
  f = 'tests/225'
data = open(f,'r').read().splitlines()

for line in data:
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

