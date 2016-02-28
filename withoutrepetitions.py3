#!/usr/bin/python3
from sys import argv
try:
  f = argv[1]
except:
  f = 'tests/173'
data = open(f,'r').read().splitlines()

for line in data:
    if not line:
        continue
    charlast=False
    out=''
    for char in line:
        if char != charlast:
            out += char
        charlast = char
    print(out)
