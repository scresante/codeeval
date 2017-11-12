#!/usr/bin/python3
from sys import argv
try:
  FILE = argv[1]
except NameError:
  FILE = 'tests/136'
DATA = open(FILE, 'r').read().splitlines()

count = 0
for line in DATA:
    if not line:
        continue
    if count == 0:
        count += 1
        pos = prev = line.index('_')
        line = line.replace('_','|')
        print(line)
        continue
    if line.find('C') != -1:
        pos = line.find('C')
    else:
        pos = line.find('_')
    line = list(line)
    if pos < prev:
        line[pos] = '/'
    elif pos == prev:
        line[pos] = '|'
    elif pos > prev:
        line[pos] = '\\'
    line = ''.join(line)
    print(line)
    prev = pos
