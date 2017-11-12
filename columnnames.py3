#!/usr/bin/python3
from sys import argv
try:
  FILE = argv[1]
except NameError:
  FILE = 'tests/197'
DATA = open(FILE, 'r').read().splitlines()

from string import ascii_uppercase
vals = list(ascii_uppercase)
from math import floor

getval = dict( [ (p,q+1) for (q,p) in enumerate(ascii_uppercase) ])
#def dec2column(num):
    #x = num % 26
    #remainder = num / 26
    #if remainder == 0:
        #return vals[x][1]
    #return dec2column(remainder) + vals[x][1]

#def dc(num):
    #x = num % 26
    ##c = ""
    ##if x < 26:
        ##c = x
    ##else:
    #c = vals[x][1]
    #if (num - x != 0):
        #return dc(num/16) + str(c)
    #else:
        #return str(c)

def trans(col):
    tot = 0
    exp = 0
    for ch in col[::-1]:
        tot += getval[ch]*26**exp
        exp += 1
    return tot

def col(num):
    orig = num
    #ret = []
    ret = ''
    if num > 26**2 + 26:
        lhs =  num/(26**2+26)
        if lhs.is_integer():
            lhs -= 0.001
        lhs = int(floor(lhs))
        if lhs == 27:
            lhs = 26
        #ret.append(vals[lhs-1])
        ret += vals[lhs-1]
        num -= lhs * 26**2
        #print(vals[lhs] + ' added, num now ' + str(num))
    if num > 26:
        lhs = ( num/26)
        if lhs.is_integer():
        # we're ending in Z
            lhs -= 0.001
        lhs = int(floor(lhs))
        #ret.append(vals[lhs-1])
        ret += vals[lhs-1]
        num -= lhs * 26**1
        #print(vals[lhs] + ' added, num now ' + str(num))
    if num > 0:
        num = int(num)
        #ret.append(vals[num-1])
        ret += vals[num-1]
    #return(''.join(ret))
    return ret

import unittest, random,pdb

class TestCol(unittest.TestCase):
    def setUp(self):
        self.seq = range(18279)
    def test_data(self):
        for line in self.seq:
            orignum = int(line)
            if orignum == 1379:
                pdb.set_trace()
            print( str(line) + ': ' + col(int(line)) )
            colname = col(orignum)
            tvalue = trans(colname)
            self.assertEqual(orignum , tvalue)
if __name__ == '__main__':
    unittest.main()
#for x in range(676,705):
##for line in DATA:
    ##if not line:
        ##continue
    ##line = int(line)
    ##pdb.set_trace()
    #line = x
    #print( str(line) + ': ' + col(line) )
