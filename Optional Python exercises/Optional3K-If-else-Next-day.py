#
# Given a month (an integer from 1 to 12) and a day in it
#   (an integer from 1 to 31) in the year 2017, print the
#   month and the day of the next day to it.
#
# 2017 was not a leap year, February had 28 days.  Set up a dictionary to hold the number of days per month
daysOfMonth = {1 : 31,2 : 28,3 : 31,4 : 30,5 : 31,6 : 30,7 : 31,8 : 31, 9: 30, 10 : 31, 11 : 30, 12 : 31}

month = int(input('Please enter the month as an integer number:'))
day = int(input('Please enter the day of the month as an integer number:'))

daysOfTheMonth = daysOfMonth[month]

if day < daysOfTheMonth:
    newDay = day + 1
else:
    newDay = 1
    newMonth = month + 1
    if newMonth > 12:
        newMonth = 1

print('The day that follows the',day,'th day of the',month,'th month,',end=' ')
print('is: the',newDay,'th day of the',newMonth,'th month.')


