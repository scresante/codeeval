#!/usr/bin/python3
from sys import argv
try:
  FILE = argv[1]
except NameError:
  FILE = 'tests/217'
DATA = open(FILE, 'r').read().splitlines()

for line in DATA:
    if not line:
        continue
    zerocount, top = [ int(q) for q in line.split(' ') ]
    lbins = [ bin(q)[2:] for q in range(1,top+1) ]
    #lbins = [ q.zfill(fillLength) for q in lbins ]
    count = 0
    for b in lbins:
        if b.count('0') == zerocount:
            count += 1;
    print(count)
