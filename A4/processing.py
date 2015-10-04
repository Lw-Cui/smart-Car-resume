#!/usr/bin/python
# -*- coding: utf-8 -*-
import xlrd
import pylab

def extract(index = 0):
	sheet = xlrd.open_workbook("CCDdata.xlsx").sheet_by_index(index)
	for rx in range(1, sheet.nrows):
		row = sheet.row(rx)
		yield int(row[2].value)


pylab.subplot(211)
y_axis = list(extract(0))
x_axis = list(range(len(y_axis)))

pylab.xlim(0, 127)
pylab.title("Grayscale Line Plot (Normal)")
pylab.ylabel("Grayscale")

pylab.plot(x_axis, y_axis, 'oy-')


pylab.subplot(212)
y_axis = list(extract(1))
x_axis = list(range(len(y_axis)))

pylab.xlim(0, 127)
pylab.title("Grayscale Line Plot (Special)")
pylab.ylabel("Grayscale")

pylab.plot(x_axis, y_axis, 'or-')

pylab.show()