from random import randint

n, p = randint(80000, 1000000), randint(20, 1000)
print("%d %d" % (n, p))
s = ""
for x in range(n):
    s += "%d " % (randint(0, 2000))
print(s.strip())


