#!/usr/bin/python3
from sys import argv
try:
  FILE = argv[1]
except NameError:
  FILE = 'tests/180'
DATA = open(FILE, 'r').read().splitlines()

cols = list('abcdefgh')

moves = [ (-2,1),
        (-2,-1),
        (-1,2),
        (-1,-2),
        (1,2),
        (1,-2),
        (2,1),
        (2,-1)]

def getpos(*tups):
    c,r = (0,0)
    for (x,y) in tups:
        c += x
        r += y
    if (c > 0 and r > 0) and (c < 9 and r < 9):
        return (c,r)

for line in DATA:
    if not line:
        continue
    col, row = line[0], line[1]
    col = cols.index(col) + 1
    row = int(row)
    valids = [ v for v in [getpos( (col,row), m) for m in moves] if v ]
# translate numerics tuples back to str chess notation
    valids = [ (cols[x-1],str(y)) for x,y in valids]
# join and sort the str list
    valids = sorted([''.join(q) for q in valids])
    print(' '.join(valids))
