#
# Given three integers, print the least of them.
#
numberA = int(input('Please, enter a number:'))
numberB = int(input('Please, enter a second number:'))
numberC = int(input('Please, enter a third number:'))

print('The minimum is:',min(numberA,numberB,numberC))


if (numberA < numberB) and (numberA < numberC):
    minNumber = numberA
elif (numberB < numberA) and (numberB < numberC):
    minNumber = numberB
elif (numberC < numberA) and (numberC < numberB):
    minNumber = numberC
    
print('The minimum number is:',minNumber)

# while we are at it, let's calculate the maximum number

print('The maximum is:',max(numberA,numberB,numberC))

if (numberA > numberB) and (numberA > numberC):
    maxNumber = numberA
elif (numberB > numberA) and (numberB > numberC):
    maxNumber = numberB
elif (numberC > numberA) and (numberC > numberB):
    maxNumber = numberC
    
print('The maximum number number is:',maxNumber)
 