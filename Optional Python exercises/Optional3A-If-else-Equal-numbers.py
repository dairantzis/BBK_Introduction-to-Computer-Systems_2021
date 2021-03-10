#
# Given three integers. Determine how many of them are equal to each other.
#   The program must print one of the numbers: 3 (if all are same), 2 (if
#   two of them are equal to each other and the third one is different) or
#   0 (if all numbers are different).
#
numberA = int(input('Please, enter a number:'))
numberB = int(input('Please, enter a second number:'))
numberC = int(input('Please, enter a third number:'))

if numberA == numberB:
    if numberB == numberC:
        print('3')
    else:
        print('2')
else:
    if numberB == numberC:
        print('2')
    else:
        print('0')
        