#!/usr/bin/python3
from sys import argv
#import itertools
#def pairwise(iterable):
    #a,b = itertools.tee(iterable)
    #next(b, None)
    #return itertools.izip(a,b)

try:
  f = argv[1]
except:
  f = 'tests/111'
data = open(f,'r').read().splitlines()

for line in data:
    if not line:
        continue
    words = sorted(line.split(' '), key = lambda x: len(x), reverse=True)
    #if len(words) == 1 or len(words[0] > words[1]):
    print(words[0])
