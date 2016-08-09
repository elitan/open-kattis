for i in xrange(int(raw_input())):
	name, began, birth, courses = raw_input().split(' ')
	began_year = int(began[:4])
	birth_year = int(birth[:4])
	courses = int(courses)
	if began_year >= 2010:
		print("%s eligible" % (name))
	elif birth_year >= 1991:
		print("%s eligible" % (name))
	elif courses >= 41:
		print("%s ineligible" % (name))
	else:
		print("%s coach petitions" % (name))
