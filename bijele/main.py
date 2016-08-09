pieces = [1, 1, 2, 2, 2, 8]
l = [ pieces[i] - x for i, x in enumerate(map(int, input().split(' '))) ]
for x in l:
    print(x, end=" ")
