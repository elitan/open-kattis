import sys
import copy

alphab_set_original = set()
for l in list("abcdefghijklmnopqrstuvwxyz"):
	alphab_set_original.add(l)

for n in xrange(int(raw_input())):
	alphab_set = copy.deepcopy(alphab_set_original)
	for l in raw_input().rstrip().lower():
		if l in alphab_set:
			alphab_set.remove(l)
	if not alphab_set:
		print("pangram")
	else:
		sys.stdout.write("missing ")
		for l in sorted(list(alphab_set)):
			sys.stdout.write(l)
		sys.stdout.write('\n')
