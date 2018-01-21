#!/usr/bin/python3
from sys import argv
try:
  FILE = argv[1]
except NameError:
  FILE = 'tests/191'
DATA = open(FILE, 'r').read().splitlines()

def normalizeLightData(raw):
    truthify = lambda x: x

# shortcuts for up, left, right, down
# avoid tuple unpacking, take them directly
def u(pos): return (pos[0]-1,pos[1])
def l(pos): return (pos[0], pos[1]-1)
def r(pos): return (pos[0], pos[1]+1)
def d(pos): return (pos[0]+1, pos[1])

def sw(x):
    if x:
        return False
    else:
        return True

def truthify(dotLights):
    # change from O/. to True/False
    blah = []
    for l in dotLights:
        blah.append([q for q in map(lambda x: x=='O', l) ])
    return blah

def untruthify(dotLights):
    # change from O/. to True/False
    blah = []
    for l in dotLights:
        blah.append([q for q in map(lambda x: '0' if x else '.' , l) ])
    return blah

def neighbors(nMax,mMax,pos):
    nCur,mCur = pos
# at origin, return down and right
    if pos == (0,0):
        return [ d(pos), r(pos) ]
# at top right
    if pos == (0, mMax):
        return [ l(pos), d(pos) ]
# at bottom right
    if pos == (nMax,mMax):
        return [ u(pos), l(pos) ]
# at bottom left
    if pos == (nMax, 0):
        return [ u(pos), r(pos) ]
# on top row
    if nCur == 0:
        return [ l(pos), d(pos), r(pos) ]
# on left column, return U, R, D
    if mCur == 0:
        return [ u(pos), r(pos), d(pos) ]
# on bottom row
    if nCur == nMax:
        return [ l(pos), u(pos), r(pos) ]
# on right row
    if mCur == mMax:
        return [ u(pos), d(pos), l(pos) ]
    return [ u(pos), r(pos), d(pos), l(pos) ]

class lights:
    box = []
    def __init__(self, lstr):
        self.box = truthify(lstr.split('|'))
## TODO move truthify functions into class
    #def __str__(self):
        #for l in untruthify(self.box):
            #return ''.join(l)
    def show(self):
        for l in untruthify(self.box):
            print(''.join(l))

    def toggle(self, n, m):
        N = len(self.box) -1
        M = len(self.box[0]) -1
        lites = self.box
        #pos = (n,m)
        #for l in lites: print(l)
        #print('switching pos :', pos)
        #print(N,M)
        #print('neighbors: ',neighbors(N,M,pos))
        for x,y in neighbors(N,M,(n,m)):
            #print('switching ',lites[n][m],'at pos: ',(n,m))
            lites[x][y] = sw(lites[x][y])
        # switch current pos light too
        #n,m = pos
        lites[n][m] = sw(lites[n][m])
        #return lites
    def isOff(self):
        # collapse the array with a comprehension and apply list(filter())
        # if the collapsed array only contains false, the result will be []
        return not list(filter(None, [item for sublist in self.box for item in sublist] ))
    def ts(self, n, m):  # shortcut for toggle and show
        self.toggle(n, m)
        self.show()

lightboxes = list()
for line in DATA:
    if not line:
        continue
    lightbox = lights (line.split(' ')[2] )
    lightboxes.append(lightbox)

