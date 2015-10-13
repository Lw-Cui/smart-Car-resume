#!/usr/bin/python
# -*- coding: utf8 -*-
from __future__ import division
import Image
import os
import numpy as np
from variable import *
from prepro import *
from func import *

# Open image file (according to stdin)
name = raw_input("Filename(bmp): ")
bmp = Image.open(name)
origin = np.array(bmp)
im = np.vectorize(extreme)(bmp.convert('L'))

# Traversal the line XMAX and try to find border line
lines = []
for i in range(0, im[XMAX].size):
	line = []
	if findline(im, (XMAX, i), line) and len(line) > 5:
		lines.append(line)
		for pair in line:
			origin[pair] = [255, 0, 0]


# Mark mid-line
step = len(lines[0]) / len(lines[1])
for i in range(len(lines[1])):
	ni = (int)(step * i)
	res = tuple([(x + y) // 2 for x, y in zip(lines[0][ni], lines[1][i])])
	origin[res] = [255, 0, 0]

origin = Image.fromarray(origin)
origin.show()
origin.save("pro" + name)
