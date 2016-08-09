import fileinput
import math

import itertools
import sys

tmp = set()
s = 'abaa'
for p in itertools.permutations(s):
	tmp.add(p)

print(math.factorial(len(s)))
print(len(tmp))

sys.exit()

for line in fileinput.input():
	line = line.strip()
	f = len(line) - len(set(list(line)))
	print(math.factorial(len(line)) / int(math.pow(2,f)))
