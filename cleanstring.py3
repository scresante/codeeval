#!/usr/bin/python3
from sys import argv
try:
  FILE = argv[1]
except NameError:
  FILE = 'tests/205'
DATA = open(FILE, 'r').read().splitlines()
import string
import re
els=[]
for line in DATA:
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
