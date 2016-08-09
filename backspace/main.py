s = input()

a_final_size = len(s) - 2 * s.count('<')
a = [''] * len(s)
i = 0

for l in s:
    if l == '<':
        i = max(0, i-1)
        continue
    else: 
        a[i] = l
    i += 1

print(''.join(a)[:a_final_size].strip())
