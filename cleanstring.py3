#!/usr/bin/python3
from sys import argv
try:
  f = argv[1]
except:
  f = 'tests/205'
data = open(f,'r').read().splitlines()
import string
import re
els=[]
for line in data:
    if not line:
        continue
    line = line.lower()
    invalid = [ x for x in (string.printable + '\\\\') if x not in string.ascii_lowercase ]
    invalid = '[' + ''.join(invalid) + ']'
    #invalid = invalid.replace('\\','\\\\')
    valid =  [ q.strip() for q in re.split(invalid, line) if q ]
    els.append(valid)
    valid = ' '.join(valid)
    #valid = valid.replace('\\','')
    print(valid)
