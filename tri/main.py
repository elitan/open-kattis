a,b,c = map(int, raw_input().split(' '))

operators = list("+-/*")
for operator in operators:
	if eval("%d%s%d" % (a,operator,b)) == c:
		print("%d%s%d=%d" % (a, operator, b, c))
		break
	if eval("%d%s%d" % (b,operator,c)) == a:
		print("%d=%d%s%d" % (a, b, operator, c))
		break