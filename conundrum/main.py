line = raw_input()

target = list("PER")

out = 0
tc = 0
for l in line:
	if l != target[tc % len(target)]:
		out += 1
	tc += 1
print(out)