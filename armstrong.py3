#!/usr/bin/python3
from sys import argv
try:
  FILE = argv[1]
except NameError:
  FILE = 'tests/82'
DATA = open(FILE, 'r').read().splitlines()

def sumofpowers(num):
    nstr = str(num)
    npow = len(nstr)
    nsum = sum( [pow(int(q),npow) for q in nstr] )
    return nsum

for line in DATA:
    if not line:
        continue
    if int(line) == sumofpowers(int(line)):
        print('True')
    else:
        print('False')
