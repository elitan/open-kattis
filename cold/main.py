raw_input()

below_zero = 0
for tmp in map(int, raw_input().split(' ')):
	below_zero += 1 * int(tmp < 0)

print(below_zero)