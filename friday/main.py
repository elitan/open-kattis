#!/bin/python
import sys

for i in xrange(int(raw_input())):
    total_days, months = map(int, list(raw_input().split(' ')))
    days_per_months = map(int, list(raw_input().split(' ')))
   
    thirteen = 0
    day = 6
    for month in xrange(months):
        for day_in_month in xrange(1, days_per_months[month] + 1):
            # print(day_in_month, day)
            if day == 4 and day_in_month == 13:
                thirteen += 1
            day = (day + 1) % 7
    print(thirteen)
