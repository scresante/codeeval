#!/usr/bin/python3
from sys import argv
try:
  FILE = argv[1]
except NameError:
  FILE = 'tests/122'
DATA = open(FILE, 'r').read().splitlines()

f = lambda x:dict([ (p,str(q)) for (q,p) in list(enumerate('abcdefghij')) ])[x]

for line in DATA:
    if not line:
        continue
    out=''
    for char in line:
        if not char.isalnum(): continue
        if char.isdigit():
            out += char
        if char.islower() and char <= 'j':
            out += f(char)
    if out == '':
        print("NONE")
    else:
        print(out)

