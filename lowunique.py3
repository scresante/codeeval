#!/usr/bin/python3
from sys import argv
try:
  FILE = argv[1]
except NameError:
  FILE = 'tests/103'
DATA = open(FILE, 'r').read().splitlines()

for line in DATA:
  if not line:
    continue
  nums = [int(q) for q in line.split(' ')]
  uniques = [q for q in nums if nums.count(q)==1]
  if uniques:
      uniques.sort()
      winner = nums.index( uniques[0] ) + 1
      print(winner)
  else:
      print(0)
