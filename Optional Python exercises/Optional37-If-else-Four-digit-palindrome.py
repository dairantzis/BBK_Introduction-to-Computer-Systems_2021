#
# Let's call an integer a _palindrome_ if it remains the same after reading its digits from right to left.
# Given a four-digit integer, print "YES" if it's a palindrome and print "NO" otherwise.
#
numberS = '' # initialise the string variable that will hold the number
while(len(numberS) != 4):
      numberS = input('Please enter a four digit integer:')

numberList = list(numberS)              # turn the string provided into a list so as to be able to compare its members
numberListReversed = numberList[::-1]   # create a new list with its contents reversed.  Start, end are empty, the step is -1

if (numberList == numberListReversed):
    print('Yes')
else:
    print('No')

# print(numberList)
# print(numberListReversed)


