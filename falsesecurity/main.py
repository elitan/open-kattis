import fileinput
import sys

def decrypt(s):
	morse_table_letters = {
		"A": ".-", 
		"B": "-...",
		"C": "-.-.",
		"D": "-..",
		"E": ".",
		"F": "..-.",
		"G": "--.",
		"H": "....",
		"I": "..",
		"J": ".---",
		"K": "-.-",
		"L": ".-..",
		"M": "--",
		"N": "-.",
		"O": "---",
		"P": ".--.",
		"Q": "--.-",
		"R": ".-.",
		"S": "...",
		"T": "-",
		"U": "..-",
		"V": "...-",
		"W": ".--",
		"X": "-..-",
		"Y": "-.--",
		"Z": "--..",
		"_": "..--",
		",": ".-.-",
		".": "---.",
		"?": "----"
	}
	morse_table_morse = {y:x for x,y in morse_table_letters.iteritems()}
	morse_code = ""
	morse_lengths = ""
	for l in s:
		morse_code += morse_table_letters[l]
		morse_lengths += str(len(morse_table_letters[l]))

	left_index = 0
	plain_text = ""
	for n in map(int, list(morse_lengths[::-1])):
		plain_text += morse_table_morse[morse_code[left_index:left_index + n]]
		left_index += n
	return plain_text


for chipher in fileinput.input():
	chipher = chipher.rstrip()
	print(decrypt(chipher))
