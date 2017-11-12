#!/usr/bin/python3
from sys import argv
try:
  FILE = argv[1]
except NameError:
  FILE = 'tests/189'
DATA = open(FILE, 'r').read().splitlines()

def median(lst):
    lst = sorted(lst)
    if len(lst) < 1:
            return None
    if len(lst) %2 == 1:
            return lst[ int(((len(lst)+1)/2)-1) ]
    else:
            return float(sum(lst[ int((len(lst)/2)-1):int((len(lst)/2)+1)]))/2.0


for line in DATA:
    if not line:
        continue
    addresses = [int(q) for q in line.split(' ')][1::]
    optimal = sum(addresses)/len(addresses)
    #distance = [abs(d - optimal) for d in addresses]
    #print ("addresses: " + str(addresses))
    #print(" mean of addresses: " + str(optimal))
    #print(" distance from each address: " + str(distance))
    #print(" sum of distances: " + str(sum(distance)) )
    med = int(round(median(addresses)))
    distance = [abs(d - med) for d in addresses]
    #print(" median of addresses: " + str(med))
    #print(" distance from each address: " + str ( distance))
    #print(" sum of distances: " + str(sum(distance)) )
    #print(" ------- ")
    print(str(sum(distance)))
