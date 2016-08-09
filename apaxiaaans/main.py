l = raw_input()
l_new = ""

prev_letter = ""
i = -1
while i < len(l)-1:
	i += 1
	if l[i] == prev_letter:
		continue
	prev_letter = l[i]
	l_new += prev_letter

print(l_new)