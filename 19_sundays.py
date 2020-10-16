import calendar


# How many Sundays fell on the first of the month
# during the twentieth century
# (1 Jan 1901 to 31 Dec 2000)?

sum =0
for year in range(1901,2001):
    for month in range(1,13):
        if (calendar.weekday(year, month, 1) == 6):
            sum = sum +1;
print(sum)