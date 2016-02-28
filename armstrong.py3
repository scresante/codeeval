#!/usr/bin/python3
from sys import argv
try:
  f = argv[1]
except:
  f = 'tests/82'
data = open(f,'r').read().splitlines()

def sumofpowers(num):
    nstr = str(num)
    npow = len(nstr)
    nsum = sum( [pow(int(q),npow) for q in nstr] )
    return nsum

for line in data:
    if not line:
        continue
    if int(line) == sumofpowers(int(line)):
        print('True')
    else:
        print('False')
