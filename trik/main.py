a, b, c = 1,0,0
for x in list(input()):
    if x == 'A':
        a, b = b, a
    elif x == 'B':
        b,c = c,b
    elif x == 'C':
        a,c = c,a
if a:
    print(1)
elif b:
    print(2)
elif c:
    print(3)
