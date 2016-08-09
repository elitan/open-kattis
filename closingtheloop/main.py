for n, _ in enumerate(xrange(int(raw_input())), 1):
	raw_input() #dont need this one

	ropes = raw_input().split(' ')
	red_bag = list()
	blue_bag = list()

	# insert to separate bags
	for rope in ropes:
		if rope[-1:] == 'R':
			red_bag.append(int(rope[:-1]))
		else:
			blue_bag.append(int(rope[:-1]))

	# sort highest first, those are the one we are going to use
	red_bag.sort(reverse=True)
	blue_bag.sort(reverse=True)

	# min length
	length = min(len(red_bag), len(blue_bag))
	red_bag = red_bag[:length]
	blue_bag = blue_bag[:length]

	print("Case #%d: %d" % (n, sum(red_bag) + sum(blue_bag) - length * 2))
