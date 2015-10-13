# -*- coding: utf8 -*-
import Image
import pylab
import numpy
from variable import *

# Get surrounding points(left, right, up, down and diagon)
def round((x, y)):
	X = [ 1,  0, -1, 1, -1,  1, 0, -1]
	Y = [-1, -1, -1, 0,  0,  1, 1,  1]
	for i in range(len(X)):
		yield (x + X[i], y + Y[i])

# Whether reach the border
def terminal((x, y)):
	return (x == XMIN or y == YMIN or y == YMAX)

# Whether this point is valid
def valid((x, y)):
	return (XMIN <= x <= XMAX and YMIN <= y <= YMAX)

visit = numpy.zeros((40, 100), dtype='bool')


# Depth-First search to find valid line
def findline(im, tuple, line):
	if terminal(tuple):
		line.append(tuple)
		return True

	for next in round(tuple):
		if valid(next) and visit[next] == False and im[next] != im[tuple]:
			visit[next] = True
			if findline(im, next, line):
				line.append(tuple)
				return True
	return False