A = list(map(int, input().split(' ')))
B = list(map(int, input().split(' ')))
C = list(map(int, input().split(' ')))

x = [A[0], B[0], C[0]]
y = [A[1], B[1], C[1]]

# x
if x.count(x[0]) > 1:
    remove = x[0]
    x = set(x)
    x.remove(remove)
    x = x.pop()
else:
    remove = x[1]
    x = set(x)
    x.remove(remove)
    x = x.pop()
# y
if y.count(y[0]) > 1:
    remove = y[0]
    y = set(y)
    y.remove(remove)
    y = y.pop()
else:
    remove = y[1]
    y = set(y)
    y.remove(remove)
    y = y.pop()

print("%d %d" % (x, y))
