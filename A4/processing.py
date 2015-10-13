#!/usr/bin/python
# -*- coding: utf-8 -*-
import pylab
from func import *

nor = list(extract(0))
spc = list(extract(1))
print "Normal border:"
print maxTuple(nor)
print "Special border:"
print maxTuple(spc)


# Draw greyscale image No.1: normal data
pylab.subplot(211)
y_axis = nor
x_axis = list(range(len(y_axis)))

pylab.xlim(0, 127)
pylab.title("Grayscale Line Plot (Normal)")
pylab.ylabel("Grayscale")

pylab.plot(x_axis, y_axis, 'oy-')


# Draw greyscale image No.2: special data
pylab.subplot(212)
y_axis = spc
x_axis = list(range(len(y_axis)))

pylab.xlim(0, 127)
pylab.title("Grayscale Line Plot (Special)")
pylab.ylabel("Grayscale")

pylab.plot(x_axis, y_axis, 'or-')

pylab.show()