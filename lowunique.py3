#!/usr/bin/python3
from sys import argv
try:
  f = argv[1]
except:
  f = 'tests/103'
data = open(f,'r').read().splitlines()

for line in data:
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
