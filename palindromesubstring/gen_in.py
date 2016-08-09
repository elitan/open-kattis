import random
import string

for x in range(100):
	a = ''.join(random.choice(string.ascii_lowercase) for _ in range(1000))
	print(a)
