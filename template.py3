#!/usr/bin/python3
from sys import argv
try:
    TEST = argv[1]
except NameError:
    TEST = 'tests'
DATA = open(TEST, 'r').read().splitlines()

for line in DATA:
    if not line:
        continue
