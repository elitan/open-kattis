s = 0
for x in range(int(input())):
    tmp = list(input())
    s += int(''.join(tmp[:-1])) ** int(''.join(tmp[-1:]))
print(s)
