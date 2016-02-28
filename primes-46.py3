#!/usr/bin/python3
from sys import argv
try:
  f = argv[1]
except:
  f = 'tests/46'
data = open(f,'r').read().splitlines()

def primes(n): 
  if n==2: return [2]
  elif n<2: return []
  s=list(range(3,n+1,2))
  mroot = n ** 0.5
  half=(n+1)/2-1
  i=0
  m=3
  while m <= mroot:
    if s[i]:
      j=int( (m*m-3)/2 )
      s[j]=0
      while j<half:
        s[j]=0
        j+=m
    i=i+1
    m=2*i+3
  return [2]+[x for x in s if x]

# get highest prime we need
top = max([int(q) for q in data])
pList = primes(top)

for line in data:
    if not line:
        continue
    upper = int(line)
    print(','.join([str(p) for p in pList if  p < upper]))
