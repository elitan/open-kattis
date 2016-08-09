import sys
#m = max(input_arr)
m = 1000000
count_arr = [0 for x in range(m + 1)]
for x in range(2, m+1):
    i = x
    sum_holder = i
    while sum_holder <= m:
        count_arr[sum_holder] += 1
        i += 1
        sum_holder += i

while True:
    n = int(input())
    if n == 0:
        # end if input, break out
        break
    print(count_arr[n])

