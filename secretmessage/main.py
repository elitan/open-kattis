import fileinput
import math
import sys

raw_input() #dont need that number

for line in fileinput.input():
	line = line.rstrip()
	K = int(math.ceil(math.sqrt(len(line))))
	M = int(math.pow(K, 2))
	line = line.ljust(M, '*')

	for i in xrange(K, 0, -1):
		row_start = M-i
		for j in xrange(row_start, K-i-1, -K):
			if line[j] != '*':
				sys.stdout.write(line[j])
	sys.stdout.write('\n')
