#!/usr/bin/python3
from sys import argv
try:
  f = argv[1]
except:
  f = 'tests/115'
data = open(f,'r').read().splitlines()


for line in data:
    if not line:
        continue
    els = line.split(',')
    words = [ e for e in els if e.isalpha() ]
    nums = [ e for e in els if e.isdigit() ]
    if words and nums:
        nums = ','.join(nums)
        words = ','.join(words) + '|'
        print(words+nums)
    elif nums:
        nums = ','.join(nums)
        print(nums)
    elif words:
        words = ','.join(words)
        print(words)
