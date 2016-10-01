import fileinput

for line in fileinput.input():
    line = line.rstrip()
    a, b = map(int, line.split(' '))
    print(abs(a-b))
