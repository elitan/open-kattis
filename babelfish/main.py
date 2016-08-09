import fileinput
import sys

d = {}
state = 1
for line in fileinput.input():
	line = line.strip()
	if state == 1:
		if not line:
			state = 2
			continue
		eng, unknown = line.split(' ')
		d[unknown] = eng
	else:
		try:
			print(d[line])
		except:
			print('eh')
