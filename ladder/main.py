import math

b, B = map(int, raw_input().split(' '))
C = 90
c = int(math.ceil((math.sin(math.radians(C)) * b) / math.sin(math.radians(B))))
print(c)