#!/usr/bin/python3
from sys import argv
from itertools import combinations
try:
  f = argv[1]
except:
  f = 'tests/81'
data = open(f,'r').read().splitlines()

for line in data:
  if not line:
    continue
  line = [int(q) for q in line.split(',')]
  print(len([q for q in combinations(line,4) if sum(q)==0]))
