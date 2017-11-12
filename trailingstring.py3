#!/usr/bin/python3
from sys import argv
try:
  FILE = argv[1]
except NameError:
  FILE = 'tests/32'
DATA = open(FILE, 'r').read().splitlines()

for line in DATA:
    if not line:
        continue
    s,e = line.split(',')
    s = s.strip()
    e = e.strip()
    if ( (s.rfind(e) + len(e)) == len(s) ) and s.rfind(e) != -1:
        print(1)
    else:
        print(0)
    #if s.rfind(e) == -1:
        #print(0)
    #else:
        #print('result of rfind: ' + str(s.rfind(e)))
        #print('len of s: ' + str(len(s)))
        #print('len of e: '+ str(len(e)))
        #print(1)
