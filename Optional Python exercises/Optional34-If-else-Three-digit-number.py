#
# Given an integer, print "YES" if it's a three-digit number and print "NO" otherwise.
#
number = int(input('Please, enter a number:'))  # make sure that an integer has been entered

# transform the number into a string
numberS = str(number)

if len(numberS) == 3:
    print('Yes')
else:
    print('No')