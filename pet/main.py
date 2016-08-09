import fileinput

c = 1
c_id = 0
c_high = 0
c_tmp = 0
for line in fileinput.input():
	c_tmp = sum(map(int, line.rstrip().split(' ')))
	if c_tmp > c_high:
		c_high = c_tmp
		c_id = c;
	c += 1

print("%d %d" % (c_id, c_high))