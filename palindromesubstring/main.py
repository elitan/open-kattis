import fileinput

def isSubPalindrom(s, i, j):
	s = s[0]
	while i <= j:
		if s[i] != s[j]:
			return False
		i += 1
		j -= 1
	return True

for line in fileinput.input():
	line = line.strip()
	line_len = len(line)
	palindroms = set()
	for i in range(0, line_len):
		for j in range(i+1, line_len):
			#print(line[i:j+1])
			if isSubPalindrom([line], i, j):
				#print('YAY', line[i:j+1])
				palindroms.add(line[i:j+1])

	for p in sorted(palindroms):
		print(p)

	print('')
