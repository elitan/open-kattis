def mean(a,b):
	return sum([x for x in xrange(a,b+1)]) / float(b-a+1)

a,b,c,d = map(int, raw_input().split(' ')) # gunnar
g_mean = mean(a,b) + mean(c,d)

a,b,c,d = map(int, raw_input().split(' ')) # emma
e_mean = mean(a,b) + mean(c,d)

if g_mean > e_mean:
	print("Gunnar")
elif g_mean < e_mean:
	print("Emma")
else:
	print("Tie")
