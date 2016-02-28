#!/usr/bin/python3
from sys import argv
try:
  f = argv[1]
except:
  f = 'tests/666'
data = open(f,'r').read().splitlines()
import string

engem = { 'a':6, 'b':12, 'c':18, 'd':24, 'e':30, 'f':36, 'g':42, 'h':48, 'i':54, 'j':60,
'k':66, 'l':72, 'm':78, 'n':84, 'o':90, 'p':96, 'q':102, 'r':108, 's':114, 't':120,
'u':126, 'v':132, 'w':138, 'x':144, 'y':150, 'z':156, } 

vals = enumerate( string.ascii_lowercase )
simple = {}
for val in vals:
    simple[val[1]] = val[0]+1

def getgemat(mapping, instring):
    value = 0
    instring = instring.lower()
    for ch in instring:
        if not ch.isalpha():
            continue
        value += mapping[ch]
    return str(value)

for line in data:
    if not line:
        continue
    print(line + ' in English Gematria equals: ' + getgemat(engem, line))
    print(line + ' in Simple Gematria equals: ' + getgemat(simple, line))

