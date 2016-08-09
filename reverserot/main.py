import fileinput

def rot(s, n):
	alphab = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ_.")
	alphab_len = len(alphab) 
	s_ret = ""
	for l in s:
		s_ret += alphab[(alphab.index(l) + n) % alphab_len]
	return s_ret

for line in fileinput.input():
	line = line.rstrip()
	if line == "0":
		break

	rot_n, plain_text = line.split(' ')
	print(rot(plain_text[::-1], int(rot_n)))
