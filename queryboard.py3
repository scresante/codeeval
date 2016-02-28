#!/usr/bin/python3
from sys import argv
try:
  f = argv[1]
except:
  f = 'tests/87'
data = open(f,'r').read().splitlines()

class Matrix(object):
    """ A simple Python matrix class with
    basic operations and operator overloading """

    def __init__(self, m, n, init=True):
        if init:
            self.rows = [[0]*n for x in range(m)]
        else:
            self.rows = []
        self.m = m
        self.n = n

    def __getitem__(self, idx):
        return self.rows[idx]

    def __setitem__(self, idx, item):
        self.rows[idx] = item

    def __str__(self):
        s='\n'.join([' '.join([str(item) for item in row]) for row in self.rows])
        return s + '\n'

    def __repr__(self):
        s=str(self.rows)
        rank = str(self.getRank())
        rep="Matrix: \"%s\", rank: \"%s\"" % (s,rank)
        return rep

    def reset(self):
        """ Reset the matrix data """
        self.rows = [[] for x in range(self.m)]

    def setRow(self, m, x):
        """ Set row #m to value x"""
        self.rows[m] = [x for nil in range(self.n) ]

    def setCol(self, n, x):
        """ Set col #n to value x """
        for row in self.rows:
            row[n] = x
    def queryRow(self, m):
        """ Returns the sum of row m """
        return sum(self.rows[m])
    def queryCol(self, n):
        """ Returns the sum of col n """
        return sum([row[n] for row in self.rows])

    def getRank(self):
        return (self.m, self.n)

    @classmethod
    def _makeMatrix(cls, rows):

        m = len(rows)
        n = len(rows[0])
        # Validity check
        if any([len(row) != n for row in rows[1:]]):
            raise(MatrixError, "inconsistent row length")
        mat = Matrix(m,n, init=False)
        mat.rows = rows

        return mat

    @classmethod
    def makeZero(cls, m, n):
        """ Make a zero-matrix of rank (mxn) """

        rows = [[0]*n for x in range(m)]
        return cls.fromList(rows)

    @classmethod
    def fromList(cls, listoflists):
        """ Create a matrix by directly passing a list
        of lists """

        # E.g: Matrix.fromList([[1 2 3], [4,5,6], [7,8,9]])

        rows = listoflists[:]
        return cls._makeMatrix(rows)


SIZE = 256
matrix = Matrix.makeZero(SIZE, SIZE)

for line in data:
    if not line:
        continue
    parts = line.split(' ')
    op = parts[0]
    q = int(parts[1])
    if len(parts) == 3:
        v = int(parts[2])
    if op == 'SetCol':
        matrix.setCol(q,v)
    if op == 'SetRow':
        matrix.setRow(q,v)
    if op == 'QueryCol':
        print(matrix.queryCol(q))
    if op == 'QueryRow':
        print(matrix.queryRow(q))
