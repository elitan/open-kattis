import fileinput

def flip_and_slip(s_len, n):
	l_index = 0
	r_index = s_len
	for i in xrange(n):
		if i % 2 == 0:
			l_index += int(s_len/4)
		else:
			r_index -= int(s_len/4)
		s_len = r_index - l_index
		if s_len < 4:
			break
	return int(l_index), int(r_index)


raw_input() #dont need that one

for data in fileinput.input():
	fs, line = data.rstrip().split(' ')
	l_index, r_index = flip_and_slip(len(line), int(fs))
	print(line[l_index:r_index])
