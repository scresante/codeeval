#!/usr/bin/python3
from sys import argv
try:
  f = argv[1]
except:
  f = 'tests/122'
data = open(f,'r').read().splitlines()

f = lambda x:dict([ (p,str(q)) for (q,p) in list(enumerate('abcdefghij')) ])[x]

for line in data:
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

