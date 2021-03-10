#
# Days of week are numbered as: 0 — Sunday, 1 — Monday,
#   2 — Tuesday, ..., 6 — Saturday. An integer K in the
#   range 1 to 365 is given. Find the number of day of week
#   for K-th day of year provided that in this year January 1 was Thursday.
#

# Setup a dictionary matching the number of the day of the week to its name
daysOfTheWeek = {0: 'Sunday', 1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday'}

daysSinceBeginning = int(input('How many days have elapsed since the beginning of the year?'))

# setup an offset of 4 because the 1st day of the year was a Thursday, which is numbered 4.
offset = 4

# The first modulo operation derives the number of the day of the week
#   with reference to the 1st of January, which was a Thursday.  The
#   offset is then added to set the day within the proper week frame.
#   However, a second modulo is required to fix the potential overflow
#   to the following week.
dayOfThisWeek = (daysSinceBeginning % 7 + offset) % 7

# use the key that was calculated above to access the content of the dictionary that was setup earlier
print('Today, is',daysOfTheWeek[dayOfThisWeek])



