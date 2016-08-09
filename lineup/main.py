team_unsorted = list()
for i in xrange(int(raw_input())):
	team_unsorted.append(raw_input().rstrip())

if team_unsorted == sorted(team_unsorted):
	print("INCREASING")
elif team_unsorted == sorted(team_unsorted, reverse=True):
	print("DECREASING")
else:
	print("NEITHER")
