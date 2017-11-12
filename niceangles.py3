#!/usr/bin/python3
""" Convert from decimal degrees to DMS format """
from sys import argv
try:
  FILE = argv[1]
except NameError:
  FILE = 'tests/160'
DATA = open(FILE, 'r').read().splitlines()
from math import floor

def toDMS(dec):
    D = int(dec)
    MS = (dec - D)*60
    M = int(MS)
    S = (MS - M)*60
    S = int(S)
    return (D,M,S)

for line in DATA:
    if not line:
        continue
    line = float(line)
    D,M,S = [str(q) for q in toDMS(line)]
    print(D + '.' + M.zfill(2) + "'" + S.zfill(2) + '"')
