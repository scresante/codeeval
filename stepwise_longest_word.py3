#!/usr/bin/python3
from sys import argv
try:
  f = argv[1]
except:
  f = 'tests/202'
data = open(f,'r').read().splitlines()

for line in data:
    if not line:
        continue
