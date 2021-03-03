#
# Given an integer greater than 9, print its last two digits.
#

number = input('Please enter an integer greater than 9:')

# use negative index to denote that only the last two digits are of interest
print(number[-2:])


