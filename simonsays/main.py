for i in xrange(int(raw_input())):
	s = raw_input()
	if s.startswith("Simon says"):
		print(s[11:])