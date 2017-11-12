#!/usr/bin/python3
from sys import argv
try:
  FILE = argv[1]
except NameError:
  FILE = 'tests/62'
DATA = open(FILE, 'r').read().splitlines()

for line in DATA:
  if not line:
    continue
  n,m = [int(q) for q in line.split(',')]
  while n >= m:
      n = n-m
  print(n)

