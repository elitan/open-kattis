n, p = list(map(int, input().split(' ')))
distribution = list(map(int, input().split(' ')))

h = 0

for i in range(n):
    tmp = 0
    for j in range(i, n):
        tmp += distribution[j] - p
        h = max(h, tmp)

print(h)
