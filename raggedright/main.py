import fileinput
import math

lines = [line.rstrip() for line in fileinput.input()]
n = 0
for line in lines:
	n = max(n, len(line))

penelty_score = 0
for line in lines[:-1]:
	if n != len(line):
		penelty_score += math.pow((n-len(line)), 2)

print(int(penelty_score))
