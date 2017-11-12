#!/usr/bin/python3
from sys import argv
try:
  FILE = argv[1]
except NameError:
  FILE = 'tests/203'
DATA = open(FILE, 'r').read().splitlines()

for line in DATA:
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
