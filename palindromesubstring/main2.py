import fileinput
import sys

# even numbers in length, no middler char to skip
def findSubPalindromsEven(palindroms, s, i):
	i, j = i, i+1
	while i >= 0 and j < len(s) and s[i] == s[j]:
		palindroms.add(s[i:j+1])
		i -= 1
		j += 1

# odd numbers in length, skip middle char
def findSubPalindromsOdd(palindroms, s, i):
	i, j = i-1, i+1
	while i >= 0 and j < len(s) and s[i] == s[j]:
		palindroms.add(s[i:j+1])
		i -= 1
		j += 1

for line in fileinput.input():
	line = line.strip()

	palindroms = set()
	for i in range(len(line)):
		findSubPalindromsEven(palindroms, line, i)
		findSubPalindromsOdd(palindroms, line, i)

	for p in sorted(palindroms):
		print(p)
	print('')
