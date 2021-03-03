#
# Given two timestamps of the same day: a number
#   of hours, minutes and seconds for both of the
#   timestamps. The moment of the first timestamp
#   happened before the moment of the second one.
#   Calculate how many seconds passed between them.
#
print('Please provide the timestamps in HH:MM:SS format')
timestamp1 = input('Please provide the first timestamp:')
timestamp2 = input('Please provide the second timestamp:')

# parse the input line to isolate the hours, minutes, seconds
timestampContents = timestamp1.split(':')   # use split to split the input to its constituents

# calculate the number of seconds within the timestamp1
timestamp1Seconds = int(timestampContents[0]) * 3600
timestamp1Seconds = timestamp1Seconds + int(timestampContents[1]) * 60
timestamp1Seconds = timestamp1Seconds + int(timestampContents[2])

# repeat for timestamp2
timestampContents = timestamp2.split(':')   # use split to split the input to its constituents

# calculate the number of seconds within the timestamp2
timestamp2Seconds = int(timestampContents[0]) * 3600
timestamp2Seconds = timestamp2Seconds + int(timestampContents[1]) * 60
timestamp2Seconds = timestamp2Seconds + int(timestampContents[2])

#calculate the difference between the two and print it.
print((timestamp2Seconds-timestamp1Seconds),'seconds elapsed from timestamp1 until timestamp2')
