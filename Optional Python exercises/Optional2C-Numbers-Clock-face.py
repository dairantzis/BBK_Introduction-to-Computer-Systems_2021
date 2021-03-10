#
# The hour hand of an analog clock turned α degrees since the midnight.
# Determine the angle by which the minute hand turned since the start of
# the current hour. Input and output in this problems are integers.
#

# There are 360 degrees in each twelve hour period.  There are 60 minutes in each hour.
#   There 12 * 60 = 720 minutes in the twelve hour period.  Therefore, as one minute
#   passes by, the hour hand moves by 360 / 720 = 0.5 degrees.
# Therefore, each minute corresponds to a 0.5 degree movement of the hour hand.
# Or, two minutes elapse for each degree of movement of the hour hand.
#
# Determine how many minutes have elapsed since midnight.
degreesSinceMidnight = int(input('How many degrees has the hour hand turned since midnight?'))

minutesSinceMidnight = degreesSinceMidnight * 2

# Determine how many minutes have elapsed since the last whole hour
minutesSinceLastHour = minutesSinceMidnight % 60

# There are 360 degrees in each hour.  There are 60 minutes in each hour.
# For each minute past the hour, the minute hand must travel 6 degrees
degreesSinceLastHour = minutesSinceLastHour * 6

print('The minutes hand has travelled',degreesSinceLastHour,'degrees, or',minutesSinceLastHour,'minutes have elapsed since the last hour')
