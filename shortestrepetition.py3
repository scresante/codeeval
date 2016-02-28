#!/usr/bin/python3
from sys import argv
import itertools
try:
  f = argv[1]
except:
  f = 'tests/107'
data = open(f,'r').read().splitlines()

for line in data:
    if not line:
        continue
    search = ''
    lastcount = 0
    length = 0
    for char in line:
        search += char
        line.count(search)
        if line.count(search) < lastcount:
            #print('something about '+search)
            length = len(search)-1
            break
        lastcount = line.count(search)
    if length == 0:
        length = len(line)
    #print(line + ': ' + str(length))
    print(length)
