data = map(int, raw_input().split(' '))

minute = ((data[0] * 60 + data[1]) - 45) % (24*60)

print("%d %d" % (minute / 60, minute % 60))