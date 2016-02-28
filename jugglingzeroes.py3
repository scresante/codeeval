#!/usr/bin/python3
from sys import argv
try:
  f = argv[1]
except:
  f = 'tests/149'
data = open(f,'r').read().splitlines()

for line in data:
    if not line:
        continue
    z = line.split(' ')
    binaryNum = '0b'
    for value,digits in list(zip(z[::2], z[1::2])):
        if value == '0':
            binaryNum += digits
        else:
            binaryNum += digits.replace('0','1')
    print( int(binaryNum, 0))
