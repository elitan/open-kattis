import fileinput

for line in fileinput.input():
	n = line.rstrip()
	if n == "0":
		break
	target = sum(map(int, list(n)))
	N = int(n)
	m = 11
	while sum(map(int, list(str(N*m)))) != target:
		m += 1
	print(m)