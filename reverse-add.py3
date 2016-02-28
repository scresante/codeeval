#!/usr/bin/python3
from sys import argv, setrecursionlimit

setrecursionlimit(100)
try:
  f = argv[1]
except:
  f = 'tests/45'
data = open(f,'r').read().splitlines()


#makesum = lambda x: str(int(x) + int(x[::-1]))

def findpalin(x, count):
    count += 1
    if x == x[::-1]:
        return (x,str(count-1))
    else:
        return (findpalin( str(int(x) + int(x[::-1])), count))
for line in data:
    if not line:
        continue
    count = 0
    print(' '.join(findpalin(line,count)[::-1]))
