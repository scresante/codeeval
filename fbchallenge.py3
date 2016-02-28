#!/usr/bin/python3
from collections import Counter
from sys import argv
import string
try:
  f = argv[1]
except:
  f = 'tests/83'
data = open(f,'r').read().splitlines()

for line in data:
    if not line:
        continue
    beauty = 0
    occs = Counter([w.lower() for w in line if w in string.ascii_letters])
    values = list(range(1,27))[::-1]
    for (letter,number) in occs.most_common():
        beauty += number * values.pop(0)
    print(beauty)

