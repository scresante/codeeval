#!/usr/bin/python3
from sys import argv
try:
  f = argv[1]
except:
  f = 'tests/40'
data = open(f,'r').read().splitlines()

def checknum(line):
    for position,value in enumerate(line):
        count = str(line.count(str(position)))
        if line[position] == count:
            pass
        else:
            return False
        return True


for line in data:
    if not line:
        continue
    if checknum(line):
        print('1')
    else:
        print('0')
