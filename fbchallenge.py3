#!/usr/bin/python3
import string
try:
  FILE = argv[1]
except NameError:
  FILE = 'tests/83'
DATA = open(FILE, 'r').read().splitlines()

from collections import Counter
from sys import argv

for line in DATA:
    if not line:
        continue
    beauty = 0
    occs = Counter([w.lower() for w in line if w in string.ascii_letters])
    values = list(range(1,27))[::-1]
    for (letter,number) in occs.most_common():
        beauty += number * values.pop(0)
    print(beauty)

