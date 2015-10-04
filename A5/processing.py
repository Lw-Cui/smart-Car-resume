#!/usr/bin/python
# -*- coding: utf8 -*-
import Image
import pylab
import numpy

def display(array):
	for i in range(array.shape[0]):
		y_axis = array[i]
		x_axis = list(range(array[0].size))
		pylab.plot(x_axis, y_axis, 'or-')
		pylab.show()

def extreme(value):
	return (0 if value < 255 / 2 else 255)

def square(value):
	return 255.0 * (value / 255.0)**2


im = pylab.array(Image.open("sBend.bmp").convert('L'))
im = numpy.vectorize(square)(im)
#display(im)

im = Image.fromarray(im)
im.show()