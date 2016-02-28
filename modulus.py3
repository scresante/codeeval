#!/usr/bin/python3
from sys import argv
try:
  f = argv[1]
except:
  f = 'tests/62'
data = open(f,'r').read().splitlines()

for line in data:
  if not line:
    continue
  n,m = [int(q) for q in line.split(',')]
  while n >= m:
      n = n-m
  print(n)

