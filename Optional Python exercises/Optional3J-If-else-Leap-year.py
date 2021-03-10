#
# Given the year number. You need to check if this year is a leap year.
#   If it is, print `LEAP`, otherwise print `COMMON`.
#
# The rules in Gregorian calendar are as follows:
#
# - a year is a leap year if its number is exactly divisible by 4 and
#   is not exactly divisible by 100
# - a year is always a leap year if its number is exactly divisible by 400
#
#**Warning.** The words `LEAP` and `COMMON` should be printed all caps.
#
year = int(input('What is the year of interest?'))

# use modulo to check whether the year is divisible by 4 and not divisible by 100
# use modulo to check whether the year is divisible by 400
if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
    print('YES')
else:
    print('NO')
    
    