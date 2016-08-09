import fileinput
import sys

n = int(raw_input()) # we dont need this one

s_1 = map(int, list(raw_input().rstrip()))
s_2 = map(int, list(raw_input().rstrip()))

zero = (0 + n) % 2
one = (1 + n) % 2

converter = {0: zero, 1: one}

c = 0
s_len = len(s_1)
while c < s_len:
    if converter[s_1[c]] != s_2[c]:
        print("Deletion failed")
        sys.exit()
    c += 1

print("Deletion succeeded")

