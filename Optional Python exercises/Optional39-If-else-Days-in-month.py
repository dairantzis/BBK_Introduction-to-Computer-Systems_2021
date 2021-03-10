#
# Given a month - an integer from 1 to 12, print the number of days in it in the year 2017.
#
# 2017 was not a leap year, February had 28 days.  Set up a dictionary to hold the number of days per month
daysOfMonth = {1 : 31,2 : 28,3 : 31,4 : 30,5 : 31,6 : 30,7 : 31,8 : 31, 9: 30, 10 : 31, 11 : 30, 12 : 31}

month = int(input('Please enter the month as an integer number:'))

print('The number of days was:',daysOfMonth[month])

print('The number of days was:',end = ' ')

if (month == 1) or (month == 3) or (month == 5) or (month == 7) or (month == 8) or (month == 10) or (month == 12):
    print('31')
elif month == 2:
    print('28')
else:
    print('30')

