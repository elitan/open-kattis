line = raw_input()

whitespace_characters = 0
lowercase_letters = 0
uppercase_letters = 0
symbols = 0

for l in line:
	ord_l = ord(l)
	if l == '_':
		whitespace_characters += 1
	elif ord_l >= 97 and ord_l <= 122:
		lowercase_letters += 1
	elif ord_l >= 65 and ord_l <= 90:
		uppercase_letters += 1
	else:
		symbols += 1

line_len = float(len(line))
print(whitespace_characters / line_len)
print(lowercase_letters / line_len)
print(uppercase_letters / line_len)
print(symbols / line_len)
