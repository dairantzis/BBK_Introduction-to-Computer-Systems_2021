# import the xor built in function from operator module
from operator import xor

# Prompt user for an integer.
inputNumber = int(input('Please provide an integer: '))

xoredNumber = xor(inputNumber, 0x55555555)  # apply the XOR operator

print(bin(inputNumber), 'XOR 0x55 yields:',bin(xoredNumber),'which in decimal is:',xoredNumber)  # and print the result

# Now, call the script again and input the output number, it should yield the one provided initially.

