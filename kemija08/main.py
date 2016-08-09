s = raw_input()
vowels = list("aeiou")

s_new = ""
i = 0
while i < len(s):
	s_new += s[i]
	if s[i] in vowels:
		i += 3
	else:
		i += 1

print(s_new)