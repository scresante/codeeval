#!/usr/bin/python3
from sys import argv
try:
  f = argv[1]
except:
  f = 'tests/106'
data = open(f,'r').read().splitlines()


def intToRoman(num):
    roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000 }
# list of tuples
    SR = sorted(roman.items(), key=lambda x: x[1], reverse=True)
# replacements (we could do the replacements algorithmically
    repls = {'IIII':'IV',
            'VIIII':'IX',
            'XIIII':'XIV',
            'LIIII':'LIV',
            'XXXX':'XL',
            'CXXXX':'CXL',
            'LXXXX':'XC',
            'CIIII':'CIV',
            'CCCC':'CD',
            'DIIII':'DIV',
            'DXXXX':'DXL',
            'DCCCC':'CM',
            'MIIII':'MIV',
            'MXXXX':'MXL',
            'MCCCC':'MCD',
            }
    out = ''
    for numeral, amount in SR:
        count = 0
        while num >= amount:
            num -= amount
            out += numeral
            count += 1
            if count > 3:
                #print('count > 3!!, last 5 in out: ', out[-5::])
                inx = out[-5::]
                out = out[:-5]
                out += repls[inx]
    return out


for line in data:
    if not line:
        continue
    num = int(line)
    out = intToRoman(num)
    #out = ''
    #for numeral, amount in SR:
        #count = 0
        #while num >= amount:
            #num -= amount
            #out += numeral
            #count += 1
            #if count > 3:
                #print('count > 3!!, last 5 in out: ', out[-5::])
                #inx = out[-5::]
                #out = out[:-5]
                #out += repls[inx]
    print(out)

