#!/usr/bin/python3
from sys import argv
try:
  FILE = argv[1]
except NameError:
  FILE = 'tests/115'
DATA = open(FILE, 'r').read().splitlines()


for line in DATA:
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
