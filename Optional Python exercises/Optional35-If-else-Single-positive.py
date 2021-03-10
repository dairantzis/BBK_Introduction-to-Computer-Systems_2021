#
# Given two non-zero integers, print "YES" if exactly one of them is positive and print "NO" otherwise.
#
numberA = 0
while(numberA == 0):
    numberA = int(input('Please enter a number:'))
    
numberB = 0
while(numberB == 0):
    numberB = int(input('Please enter another number:'))
    
print(numberA)
print(numberB)

# if the logical xor of the two boolean expressions is true, then...
if (numberA > 0) ^ (numberB > 0):
    print('Yes')
else:
    print('No')


