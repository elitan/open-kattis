import sys

r, n = list(map(int, input().split(' ')))
booked = set()
for _ in range(n):
    booked.add(int(input()))

for i in range(1, r+1):
    if i not in booked:
        print(i)
        sys.exit()

print('too late')

