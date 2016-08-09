import fileinput

problems = dict()

solved, time = 0, 0
for line in fileinput.input():
	line = line.rstrip()
	if line == "-1":
		break
	minutes, problem, rw = line.split(' ')	
	if rw == "wrong":
		try:
			problems[problem] += 1
		except:
			problems[problem] = 1
	else:
		solved += 1
		time += int(minutes)
		try:
			time += 20 * problems[problem]
		except:
			pass
print("%d %d" % (solved, time))