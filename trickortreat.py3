#!/usr/bin/python3
from sys import argv
try:
  FILE = argv[1]
except NameError:
  FILE = 'tests/220'
DATA = open(FILE, 'r').read().splitlines()
from math import floor
import re
for line in DATA:
    if not line:
        continue
    prog = re.match("Vampires: (?P<V>\d+), Zombies: (?P<Z>\d+), Witches: (?P<W>\d+), Houses: (?P<H>\d+)", line)
    vals = prog.groupdict()
    candies = ( int(vals['V'])*3 + int(vals['Z'])*4 + int(vals['W'])*5 ) * int(vals['H'])
    children = int(vals['V']) + int(vals['Z']) + int(vals['W'])
    print(floor(candies/children))

