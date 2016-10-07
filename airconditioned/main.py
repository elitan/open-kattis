import fileinput
import sys

def findSpan(spans, new_span):
    a, b = new_span
    for span in spans:
        if a >= span[0] and b <= span[1]:
            a, b = span
            return True
        elif a < span[0] and b > span[1]:
            return True
        elif a >= span[0] and a <= span[1]:
            span[0] = a
            return True
        elif b >= span[0] and b <= span[1]:
            span[1] = b
            return True
    return False

spans = []

input() # dont need first number
for line in fileinput.input():
    line = line.rstrip()
    new_span = list(map(int, line.split(' ')))

    if not findSpan(spans, new_span):
        spans.append(new_span)

print(len(spans))
