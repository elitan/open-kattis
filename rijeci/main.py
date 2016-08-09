a,b = 1,0
a_tmp, b_tmp = 1, 0
for i in xrange(int(raw_input())):
	b_tmp += a # A -> B
	a_tmp -= a # A -> B

	a_tmp += b # B -> BA

	a,b = a_tmp, b_tmp
print("%d %d" % (a,b))