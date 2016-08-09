lines = int(raw_input())

for i in xrange(lines):
	line = int(raw_input())
	print("%d is %s" % (line, "even" if line % 2 == 0 else "odd"))