import fileinput
import sys

sentence = ""
word_bag = set()
for line in fileinput.input():
	words = line.rstrip().split(' ')

	for word in words:
		if word.lower() in word_bag:
			sys.stdout.write('. ')
		else:
			word_bag.add(word.lower())
			sys.stdout.write("%s " % word)
	sys.stdout.write('\n')
