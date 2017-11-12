#!/usr/bin/python3
from sys import argv
try:
  FILE = argv[1]
except NameError:
  FILE = 'tests/227'
DATA = open(FILE, 'r').read().splitlines()

for line in DATA:
    if not line:
        continue
    nums = list( [ int(q) for q in line.replace(' ','') ] )
    summed = sum(nums[::2])
    if (sum(nums[1::2]) + summed*2)%10 == 0:
        print('Real')
    else:
        print('Fake')



