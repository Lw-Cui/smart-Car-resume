# -*- coding: utf8 -*-
import Image
import pylab
import numpy
import Queue
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


# Breadth-First search for image processing
def findline_BFS(im, tp, line):
	prev = numpy.ndarray((40, 100), dtype=tuple)
	q = Queue.Queue()
	q.put(tp)
	visit[tp] = True


	while q.empty() != True:
		now = q.get()
		for next in round(now):
			if valid(next) and visit[next] == False and im[next] != im[now]:
				visit[next] = True
				prev[next] = now
				q.put(next)
				if terminal(next):
					while prev[next] != None:
						line.append(next)
						next = prev[next]
					return True

	return False


