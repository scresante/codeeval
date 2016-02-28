#!/usr/bin/python3
from sys import argv
try:
  f = argv[1]
except:
  f = 'tests/166'
data = open(f,'r').read().splitlines()

import datetime

for line in data:
    if not line:
        continue
    t1, t2 = line.split(' ')
    #print(t1 + '|' + t2)
    t1 = [1,1,1] + [int(q) for q in t1.split(":")]
    t2 = [1,1,1] + [int(q) for q in t2.split(":")]
    d1 = datetime.datetime(*t1)
    d2 = datetime.datetime(*t2)
    h, m, s = str(abs(d1-d2)).split(':')
    h = h.zfill(2)
    print(':'.join((h,m,s)))
