#
# Given a year (as a positive integer), find the respective number
#  of the century. Note that, for example, 20th century began with
#  the year 1901.
#
year = int(input('What is the year?'))

# floor division of x // y returns the largest integer less than or equal to x / y
#   we need to add one to adjust for the first century
century = (year // 100) + 1

print('The century is:',century)
