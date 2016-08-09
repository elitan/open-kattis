import math

s = map(int, list(raw_input()))
zoom_level = len(s)
size = int(math.pow(2, zoom_level))

x = y = 0
for n in s:
	size /= 2
	if n == 0:
		continue
	elif n == 1:
		x += size
	elif n == 2:
		y += size
	else:
		x += size
		y += size
	#print("current i: %d, j: %d" % (i, j))
print("%d %d %d" % (zoom_level, x, y))

"""
130
x = 2^3 = 8

# 1
i,j = 0,0
0 ->	i += 0.0 # stand still
1 ->	i += x/2 #move right ##<<
2 ->	j += x/2 #move down
3 ->	i,j += x/2 #move diagonaly


i,j = 4,0
x = x/2 = 4
# 3
0 ->	i += 0.0 # stand still
1 ->	i += x/2 #move right
2 ->	j += x/2 #move down
3 ->	i,j += x/2 #move diagonaly

i,j = 6,2
x = x/2 = 2
# 0
0 ->	i += 0.0 # stand still

# got it :) No, lets just implement it
"""
