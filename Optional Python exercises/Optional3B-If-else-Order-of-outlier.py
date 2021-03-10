#
# Given three integers, in which two are equal to each other and the third one is different.
#   Print the order number of this different one - 1, 2 or 3.
#
numberA = int(input('Please, enter a number:'))
numberB = int(input('Please, enter a second number:'))
numberC = int(input('Please, enter a third number:'))

if numberA == numberB == numberC:
    print('All three numbers are equal!')
else:
    if numberA == numberB:
        print('3')
    elif numberA == numberC:
        print('2')
    elif numberB == numberC:
        print('1')