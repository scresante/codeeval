#!/usr/bin/python3
from sys import argv
try:
  FILE = argv[1]
except NameError:
  FILE = 'tests/167'
DATA = open(FILE, 'r').read().splitlines()

for line in DATA:
    #print(line)
    #print('.........1.........2.........3.........4.........5....x....6')
    if not line:
        continue
    if len(line) <= 55:
        print(line)
        continue
    line = line[:40]
    stop = line.rfind(' ')
    if stop != -1:
        line = line[:stop] + '... <Read More>'
    print(line)
