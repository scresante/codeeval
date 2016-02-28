#!/usr/bin/python3
from sys import argv
try:
  f = argv[1]
except:
  f = 'tests/186'
data = open(f,'r').read().splitlines()
for line in data:
    if not line:
        continue
    stride, nums = line.split(';')
    stride = int(stride)
    nums = [ int(q) for q in nums.split(' ') ]
    groups = len(nums) - stride + 1
    #print(nums)
    gains = []
    for g in range(groups):
        #print(nums[g:stride+g])
        gains.append(sum(nums[g:stride+g]))
    
    #print(max(gains))
    if max(gains) < 0:
        print(0)
    else:
        print(max(gains))
