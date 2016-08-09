import sys

set_id = 1
while True:
	nr_of_names = int(raw_input())
	if nr_of_names == 0:
		break

	#fix order
	new_name_list = list()	
	group_id = 0
	for i in xrange(nr_of_names):
		name = raw_input()
		if i % 2 == 0:
			new_name_list.insert(group_id, name)
			group_id += 1
		else:
			new_name_list.insert(group_id, name)

	print("SET %d" % (set_id))
	for name in new_name_list:
		print(name)

	set_id += 1
