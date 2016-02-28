#!/usr/bin/python3
from sys import argv
try:
  f = argv[1]
except:
  f = 'tests/132'
data = open(f,'r').read().splitlines()
from itertools import groupby

def major(line):
    groups = [ list(g) for k, g in groupby(line) ]
    for g in groups:
        if len(g) > len(line)/2:
            return g[0]
    return 'None'

for line in data:
    if not line:
        continue
    line = sorted([q for q in line.split(',')])
    print(major(line))
