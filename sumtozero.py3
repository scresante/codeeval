#!/usr/bin/python3
from sys import argv
from itertools import combinations
try:
  FILE = argv[1]
except NameError:
  FILE = 'tests/81'
DATA = open(FILE, 'r').read().splitlines()

for line in DATA:
  if not line:
    continue
  line = [int(q) for q in line.split(',')]
  print(len([q for q in combinations(line,4) if sum(q)==0]))
