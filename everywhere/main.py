test_cases = int(raw_input())

for i in range(test_cases):
	cs = set()
	cities = int(raw_input())
	for j in range(cities):
		cs.add(raw_input())
	print(len(cs))