#!/usr/bin/python3
from sys import argv
#import timeit
import itertools
data = open(argv[1],'r').read().splitlines()

TR = {\
     0:('0'), 1:('1'),
     2:('a','b','c'), 3:('d','e','f'), 4:('g','h','i'), 5:('j','k','i'),
     6:('m','n','o'), 7:('p','q','r','s'), 8:('t','u','v'), 9:('w','x','y','z')
     }
results=[]
def collect(ar):
  results.append(''.join(ar))


def main(line): #this is looped from input
# line is defined to be a number mapping to the dictionary
# each number in the line is iterated through all possible combos
#  print('this is a new shot for ', line)
  line = [int(a) for a in list(line)]
  out=[]
  for num in list(line):
    a=[]
    for ch in TR[num]:
      a.append(ch)
    out.append(a)
  o = []

  for x in (itertools.product(*out)):
    collect(x)

for line in data:
  if not line:
    continue
  #print(line)
  main(line)
#  timeit.Timer(main(line)).timeit()
  print(','.join(results))
