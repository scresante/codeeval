#!/usr/bin/python3
from sys import argv
try:
  f = argv[1]
except:
  f = 'tests/203'
data = open(f,'r').read().splitlines()

for line in data:
    if not line:
        continue
    count = 0 
    stride = 5
    groups = len(line) - stride + 1
    for g in range(groups):
        cut = line[g:stride+g]
        if cut == '<--<<' or cut == '>>-->':
            count += 1
    print(count)
