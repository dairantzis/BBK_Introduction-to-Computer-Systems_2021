#
# Given a positive real number,
#   print its first digit to the right of the decimal point.
#
number = input('Please enter a positive real number:')

# split the input number in two, using the '.' as their separator
splitNumber = number.split('.')

# now print the first character of the decimal part
# remember that strings are 0 based, so the 1st number
# has an index of 0
decimalPart = splitNumber[1]
print('The first digit of the decimal part is:',decimalPart[0])
