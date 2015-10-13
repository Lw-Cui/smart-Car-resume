# -*- coding: utf-8 -*-
import xlrd
import pylab

BLACK = 0
WHITE = 255

# Generator: extract info from .xlsx and return it one by one
def extract(index = 0):
	sheet = xlrd.open_workbook("CCDdata.xlsx").sheet_by_index(index)
	for rx in range(1, sheet.nrows):
		row = sheet.row(rx)
		yield int(row[2].value)


# Generator: find all tuple range from first white to last white.
def allTuple(line):
	start = -1
	for inx, val in enumerate(line):
		if start == -1 and val == WHITE:
			start = inx
		elif start != -1 and val == BLACK:
			yield (start, inx - 1)
			start = -1

# Geryscle transform
def pro(x):
	return WHITE if x > 128 / 2 else BLACK

# Find max interval
def maxTuple(line):
	max = (0, 0)
	for t in allTuple(map(pro, line)):
		if t[1] - t[0] > max[1] - max[0]:
			max = t
	return max