#
# Given the integer N - the number of minutes that is passed since midnight
#   - how many hours and minutes are displayed on the 24h digital clock?
# The program should print two numbers: the number of hours (between 0 and 23)
#   and the number of minutes (between 0 and 59).
#
# For example, if N = 150, then 150 minutes have passed since midnight - i.e. now
#   is 2:30 am. So the program should print `2 30`.
#
minutesSinceMidnight = int(input('How many minutes elapsed since midnight?'))

# Calculate the number of hours - use floor division
hours = minutesSinceMidnight // 60

# Calculate the number of minutes - use modulo
minutes = minutesSinceMidnight % 60

if hours == 1:
    print(hours,'hour,',end='')
else:
    print(hours,'hours,',end='')

print(' and',minutes,end=' ')

if minutes == 1:
    print('minute',end='')
else:
    print('minutes',end='')

print(', have passed since midnight.')

