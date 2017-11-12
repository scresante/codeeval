#!/usr/bin/python3
from sys import argv
try:
  FILE = argv[1]
except NameError:
  FILE = 'tests/131'
DATA = open(FILE, 'r').read().splitlines()

for line in DATA:
    if not line:
        continue
    nums, op = line.split(' ')
    keys = op.replace('+','').replace('-','')
    mapping = dict(zip(keys, nums))
    opeval = ''
    operator = ''
    for char in op:
        if char in mapping:
            opeval += mapping[char]
        else:
            opeval += char
            operator = char
    opleft, opright = [str(int(q)) for q in opeval.split(operator)]
    print(str(eval(opleft + operator + opright) ))
