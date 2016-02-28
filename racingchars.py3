#!/usr/bin/python3
from sys import argv
try:
  f = argv[1]
except:
  f = 'tests/136'
data = open(f,'r').read().splitlines()

count = 0
for line in data:
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
