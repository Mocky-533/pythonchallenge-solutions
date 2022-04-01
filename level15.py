import calendar

front, count = 2000, 0
while True:
    year = front + 6
    if calendar.isleap(year) and calendar.weekday(year, 1, 1) == 3:
        count += 1
    front -= 10
    if count == 2:
        print(year)
        break
