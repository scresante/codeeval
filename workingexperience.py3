#!/usr/bin/python3
from sys import argv
try:
  FILE = argv[1]
except NameError:
  FILE = 'tests/139'
DATA = open(FILE, 'r').read().splitlines()

from math import floor

def dateToMonth(dstring):
    """ Translate Date to a month# with jan 1990 = 0 """
    months = { "Jan": 0, "Feb": 1, "Mar": 2, "Apr": 3, "May": 4, "Jun": 5, "Jul": 6,
            "Aug": 7, "Sep": 8, "Oct": 9, "Nov": 10, "Dec": 11}
    a, b = dstring.split(' ')
    yr = int(b)
    mo = months[a]
    return mo + (yr - 1990)*12

for line in DATA:
    if not line:
        continue
    periods = line.split(';')
    exp = []
    for period in periods:
        period = period.strip()
        start, end = [ dateToMonth(q) for q in period.split('-') ]
        #exp.append( (start,end) )
        exp += list(range(start,end+1))

    print(floor(len(set(exp))/12))
