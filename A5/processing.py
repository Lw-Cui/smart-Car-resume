#!/usr/bin/python
# -*- coding: utf8 -*-
import func
import Image
import pylab
import numpy

#FILE = "lBend.bmp"
FILE = "sBend.bmp"
im = pylab.array(Image.open(FILE).convert('L'))
im = numpy.vectorize(func.extreme)(im)

origin = pylab.array(Image.open(FILE).convert('L'))
#func.display(origin[-1])

for i in range(0, im[-1].size):
	if func.getline(im, (-1, i)):
		print func.line
		for tuple in func.line: 
			origin[tuple] = func.BLACK

origin = Image.fromarray(origin)
origin.show()
