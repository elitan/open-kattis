import fileinput
import math
import sys

for line in fileinput.input():
	r,m,c = map(float, line.rstrip().split(' '))
	if r+m+c == 0:
		break

	true_area = "{0:.8f}".format(r*r*math.pi)
	estimate_area = "{0:.8f}".format(math.pow(r+r, 2) * (c / m))
	print("%s %s" % (true_area, estimate_area))
