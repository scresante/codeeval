#!/usr/bin/python3
from sys import argv
try:
  f = argv[1]
except:
  f = 'tests/217'
data = open(f,'r').read().splitlines()

for line in data:
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
