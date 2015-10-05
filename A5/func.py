# -*- coding: utf8 -*-
import Image
import pylab
import numpy

WHITE = 255
BLACK = 0

def display(array):
	y_axis = array
	x_axis = list(range(array.size))
	pylab.plot(x_axis, y_axis, 'or-')
	pylab.show()

def extreme(value):
	return (BLACK if value < WHITE / 2 else WHITE)

def square(value):
	return WHITE * (value / WHITE)**2

def round((x, y)):
	X = [ 1,  0, -1, 1, -1,  1, 0, -1]
	Y = [-1, -1, -1, 0,  0,  1, 1,  1]
	for i in range(len(X)):
		yield (x + X[i], y + Y[i])

def terminal((x, y)):
	return (x == -40 or y == 0 or y == 99)

def valid((x, y)):
	return (-40 <= x <= -1 and 0 <= y <= 99)

line = []
visit = numpy.zeros((40, 100), dtype='bool')

def getline(im, tuple):
	if terminal(tuple):
		line.append(tuple)
		return True

	#print tuple, '--->', list(round(tuple))
	for next in round(tuple):
		if valid(next) and visit[next] == False and im[next] != im[tuple]:
			visit[next] = True
			if getline(im, next):
				line.append(tuple)
				return True
	return False