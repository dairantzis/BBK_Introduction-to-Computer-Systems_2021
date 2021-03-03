

# Given the integer N - the number of seconds that have passed
#   since midnight - how many full hours and full minutes have
#   passed since midnight?
# The program should print two numbers: the number of hours (between
#   0 and 23) and the number of minutes (between 0 and 1339).
#
# For example, if N = 3900, then 3900 seconds have passed since
#   midnight - i.e. now it's 1:05am. So the program should print
#   1 65 - 1 full hour passed since midnight, 65 full minutes
#   passed since midnight.

seconds = int(input('How many seconds passed by since midnight?'))

minutes = seconds // 60
hours = minutes // 60

if hours == 1:
    print(hours,'hour,',end='')
else:
    print(hours,'hours,',end='')

print(' or',minutes,'minutes, have passed since midnight.')