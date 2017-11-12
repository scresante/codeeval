#!/usr/bin/python3
from sys import argv
try:
  FILE = argv[1]
except NameError:
  FILE = 'tests/226'
DATA = open(FILE, 'r').read().splitlines()

global lookup;
lookup = {
'a':'u',
'b':'v',
'c':'w',
'd':'x',
'e':'y',
'f':'z',
'g':'n',
'h':'o',
'i':'p',
'j':'q',
'k':'r',
'l':'s',
'm':'t',
'n':'g',
'o':'h',
'p':'i',
'q':'j',
'r':'k',
's':'l',
't':'m',
'u':'a',
'v':'b',
'w':'c',
'x':'d',
'y':'e',
'z':'f',
}

def decode(line):
    out = ''
    for char in list(line):
        out += lookup[char]
    return out

for line in DATA:
    if not line:
        continue
    out = ''
    for char in list(line):
        out += lookup[char]
    print(out)
