#!/usr/bin/python3
from sys import argv
try:
  f = argv[1]
except:
  f = 'tests/227'
data = open(f,'r').read().splitlines()

for line in data:
    if not line:
        continue
    nums = list( [ int(q) for q in line.replace(' ','') ] )
    summed = sum(nums[::2])
    if (sum(nums[1::2]) + summed*2)%10 == 0:
        print('Real')
    else:
        print('Fake')



