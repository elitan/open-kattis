case_id = 1
for n in xrange(int(raw_input())):
	raw_input() # dont need that number
	control_dict = dict()
	control_set = set()
	numbers = map(int, raw_input().split(' '))
	for inv_number in numbers:
		control_set.add(inv_number)
		try:
			control_dict[inv_number] += 1
			control_set.remove(inv_number)
		except:
			control_dict[inv_number] = 1
	print("CASE #%d: %d" % (case_id, control_set.pop()))
	case_id += 1
