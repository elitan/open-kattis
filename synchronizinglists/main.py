import sys

n = int(raw_input())
while True:

	list_a = list()
	list_map = dict()
	for i in xrange(n):
		list_a.append(int(raw_input()))
	for i, j in enumerate(sorted(list_a)):
		list_map[i] = list_a.index(j)

	list_b = list()
	list_b_correct = [0 for x in xrange(n)]
	for i in xrange(n):
		list_b.append(int(raw_input()))
	for i, j in enumerate(sorted(list_b)):
		list_b_correct[list_map[i]] = j

	for i in list_b_correct:
		print(i)

	n = int(raw_input())
	if n == 0:
		break

	print("")
