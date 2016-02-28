#!/usr/bin/python3
from sys import argv
try:
  f = argv[1]
except:
  f = 'tests/128'
data = open(f,'r').read().splitlines()
from itertools import groupby
for line in data:
    if not line:
        continue
    groups = [ list(g) for k, g in groupby(line.split(' ')) ]
    print( ' '.join([ (str(len(w)) + ' ' + w[0]) for w in groups ]) )

