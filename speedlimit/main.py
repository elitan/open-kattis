while True:
	lines = int(raw_input())
	if lines == -1:
		break

	prev_duration = 0
	miles = 0
	for i in xrange(lines):
		speed, duration = map(int, raw_input().split(' '))
		duration -= prev_duration
		prev_duration += duration
		miles += speed * duration
	print("%d miles" % (miles))