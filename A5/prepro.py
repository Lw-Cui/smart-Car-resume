# -*- coding: utf8 -*-
import pylab
from variable import *

#display grayscale image
def display(array):
	y_axis = array
	x_axis = list(range(array.size))
	pylab.plot(x_axis, y_axis, 'or-')
	pylab.show()

# Grayscale transform function
def extreme(value):
	return (BLACK if value < WHITE // 1.5 else WHITE)

def square(value):
	return WHITE * (value / WHITE)**2
