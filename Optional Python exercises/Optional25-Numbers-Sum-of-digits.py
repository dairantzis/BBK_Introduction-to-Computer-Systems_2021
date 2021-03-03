#
# Given a three-digit number. Find the sum of its digits.
#
number = input('Please enter an integer number:')

sumOfDigits = 0    # initialise the variable that will hold the sum
for c in number:   # go through all the digits of the string entered

    # turn each character into an integer and add it to the sum
    sumOfDigits = sumOfDigits + int(c)
    
print('The sum of the digits of the number is:',sumOfDigits)
