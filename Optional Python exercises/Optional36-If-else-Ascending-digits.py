#
# Given a three-digit integer X consisting of three different digits,
#   print "YES" if its three digits are going in an ascending order from
#   left to right and print "NO" otherwise.
#
numberS = '' # initialise the string variable that will hold the number
while(len(numberS) != 3):
      numberS = input('Please enter a three digit integer:')

numberList = list(numberS)  # turn the string provided into a list so as to be able to compare its members

if (numberList[0] < numberList[1] < numberList[2]):
    print('Yes')
else:
    print('No')
