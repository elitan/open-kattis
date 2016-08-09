import fileinput

for line in fileinput.input():
	if line.rstrip() == "0 0":
		break
	numerator, denominator = map(int, line.rstrip().split(' '))
	print("%d %d / %d" % (numerator / denominator, numerator % denominator, denominator))