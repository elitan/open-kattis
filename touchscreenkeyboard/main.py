#/bin/python
import binascii
import sys

def key_distance(w1, w2, keyboard):
    word_len = len(w1)
    i = 0
    distance = 0
    while i < word_len:
        x,y = map(int, keyboard[w1[i]].split(','))
        a,b = map(int, keyboard[w2[i]].split(','))
        distance += abs(x-a) + abs(y-b)
        i += 1
    return distance


# fix keyboard
key_tmp = list()
key_tmp.append(list("qwertyuiop"))
key_tmp.append(list("asdfghjkl"))
key_tmp.append(list("zxcvbnm"))

keyboard = dict()

for i, keyline in enumerate(key_tmp):
    for j, key in enumerate(keyline):
        keyboard[key] = "%d,%d" % (i, j)

# start program
for _ in range(int(input())):
    word, tests = input().split(' ') # word to test
    tests = int(tests)

    word_dict = dict()
    word_list = list()
    word_list_order = list()

    # check each word
    for __ in range(tests):
        match_word = input()
        distance = key_distance(word, match_word, keyboard)
        s = "%d%s" % (distance, match_word)
        s = int(binascii.hexlify(s.encode('ascii')), 16)
        #s = int(s.encode('hex'), 16)
        word_dict[s] = "%d.%s" % (distance, match_word)
    
    # sort words
    for key, value in sorted(word_dict.items()):
        distance, word = value.split('.')
        print("%s %s" % (word, distance))
