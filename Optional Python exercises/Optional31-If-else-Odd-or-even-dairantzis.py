#
# Given an integer, print "odd" if it's odd and print "even" otherwise.
#
number = int(input('Please enter a number:'))

print('The number is:',end='')

if number % 2 == 0:
    print('even')
else:
    print('odd')
    