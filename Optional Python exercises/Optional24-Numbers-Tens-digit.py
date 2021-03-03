#
# Given an integer, print its tens digit.
#
number = input('Please enter an integer greater than 9:')

# the decades digits is of interest, therefore print
#   the input string from an index of -2 to an index of -1
#   remember that the end character of the range is not
#   printed in Python
print('The decades digit is:',number[-2:-1])