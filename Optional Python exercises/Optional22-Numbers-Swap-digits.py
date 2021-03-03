#
# Given a two-digit integer, swap its digits and print the result.
#

number = (input('Please enter a two digit integer:'))

while len(number) < 2:        # ensure that there are two digits in the number
    number = ' ' + number

# strings are immutable, therefore, the two characters need to be
#   assigned to a new string
newnumber = number[1] + number[0]

# which is then print
print('The new number is:',newnumber)

