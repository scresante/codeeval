#!/usr/bin/python3
from sys import argv
try:
  FILE = argv[1]
except NameError:
  FILE = 'tests/132'
DATA = open(FILE, 'r').read().splitlines()
from itertools import groupby

def major(line):
    groups = [ list(g) for k, g in groupby(line) ]
    for g in groups:
        if len(g) > len(line)/2:
            return g[0]
    return 'None'

for line in DATA:
    if not line:
        continue
    line = sorted([q for q in line.split(',')])
    print(major(line))
