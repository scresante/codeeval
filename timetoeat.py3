#!/usr/bin/python3
from sys import argv
import datetime
try:
  f = argv[1]
except:
  f = 'tests/214'
data = open(f,'r').read().splitlines()

for line in data:
    if not line:
        continue
    times = line.split(' ')
    dt = []
    for t in times:
        dt.append(datetime.datetime( *([1,1,1] + [int(q) for q in t.split(":")])) )
    dt.sort(reverse=True)
    print( ' '.join([ str(x).split(" ")[1] for x in dt ] ) )
