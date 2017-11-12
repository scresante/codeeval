#!/usr/bin/python3
from sys import argv
try:
  FILE = argv[1]
except NameError:
  FILE = 'tests/128'
DATA = open(FILE, 'r').read().splitlines()
from itertools import groupby
for line in DATA:
    if not line:
        continue
    groups = [ list(g) for k, g in groupby(line.split(' ')) ]
    print( ' '.join([ (str(len(w)) + ' ' + w[0]) for w in groups ]) )

