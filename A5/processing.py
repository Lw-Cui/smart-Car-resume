#!/usr/bin/python
# -*- coding: utf8 -*-
import Image
import pylab

im = pylab.array(Image.open("lBend.bmp").convert('L'))
'''
for i in range(40):
	y_axis = im[i]
	x_axis = list(range(im[0].size))
	pylab.plot(x_axis, y_axis, 'or-')
	pylab.show()
'''

for i in range(im.shape[0]):
	for j in range(im[i].size):
		if im[i][j] < 255 / 2:
			im[i][j] = 0
		else:
			im[i][j] = 255

im = Image.fromarray(im)
im.show()
