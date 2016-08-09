#each digit is 3 size width

import fileinput
import time
import sys
import copy
import math

def list_to_number(l, number_profiles):
    for i, profile in enumerate(number_profiles):
        if l == profile:
            return i
    return -1

# read numbers from raw
numbers_raw = """***   * *** *** * * *** *** *** *** ***
* *   *   *   * * * *   *     * * * * *
* *   * *** *** *** *** ***   * *** ***
* *   * *     *   *   * * *   * * *   *
***   * *** ***   * *** ***   * *** ***"""

number_raw_grid = [list(x) for x in numbers_raw.split('\n')]

number_profiles = list()
i = 0
while i < 10:
    number_raw_tmp = list()
    number_list = list()

    for line in number_raw_grid:
        number_list.append(line[0:3])
        number_raw_tmp.append(line[4:])

    number_profiles.append(copy.deepcopy(number_list))
    number_raw_grid = number_raw_tmp
    i += 1


# start the program
number_grid = list()

for line in fileinput.input():
    number_grid.append(list(line.rstrip('\n')))

i = 0
iterations = math.ceil(len(number_grid[0]) / 4.0)
number_s = ""
while i < iterations:
    number_list = list()
    number_grid_tmp = list()

    for line in number_grid:
        number_list.append(line[0:3])
        number_grid_tmp.append(line[4:])

    number_s += str(list_to_number(number_list, number_profiles))

    number_grid = number_grid_tmp
    i += 1

if "-1" in number_s:
    print("BOOM!!")
elif int(number_s) % 6 == 0:
    print("BEER!!")
else:
    print("BOOM!!")
