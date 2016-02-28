#!/usr/bin/python3
""" Convert from decimal degrees to DMS format """
from sys import argv
try:
  f = argv[1]
except:
  f = 'tests/160'
data = open(f,'r').read().splitlines()
from math import floor

def toDMS(dec):
    D = int(dec)
    MS = (dec - D)*60
    M = int(MS)
    S = (MS - M)*60
    S = int(S)
    return (D,M,S)

for line in data:
    if not line:
        continue
    line = float(line)
    D,M,S = [str(q) for q in toDMS(line)]
    print(D + '.' + M.zfill(2) + "'" + S.zfill(2) + '"')
