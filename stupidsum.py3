#!/usr/bin/python
from sys import argv
data = open(argv[1],'r').read().splitlines()

for line in data:
  if not line: continue
  print sum([int(q) for q in list(line)])
