import fileinput
import sys

player = int(raw_input())
game_time = 0
raw_input() # not needed

for line in fileinput.input():
    line = line.rstrip()
    time, answer = line.split(' ')
    time = int(time)
    game_time += time

    if game_time >= 210:
        print(player)
        sys.exit()

    if answer == 'T':
        player = max(1, ((player + 1) % 9))
