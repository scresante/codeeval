#!/usr/bin/python3
from sys import argv
try:
  FILE = argv[1]
except NameError:
  FILE = 'tests/111'
DATA = open(FILE, 'r').read().splitlines()

#import itertools
#def pairwise(iterable):
    #a,b = itertools.tee(iterable)
    #next(b, None)
    #return itertools.izip(a,b)

for line in DATA:
    if not line:
        continue
    words = sorted(line.split(' '), key = lambda x: len(x), reverse=True)
    #if len(words) == 1 or len(words[0] > words[1]):
    print(words[0])
