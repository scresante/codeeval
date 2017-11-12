#!/usr/bin/python3
from sys import argv
try:
  FILE = argv[1]
except NameError:
  FILE = 'tests/40'
DATA = open(FILE, 'r').read().splitlines()

def checknum(line):
    for position,value in enumerate(line):
        count = str(line.count(str(position)))
        if line[position] == count:
            pass
        else:
            return False
        return True


for line in DATA:
    if not line:
        continue
    if checknum(line):
        print('1')
    else:
        print('0')
