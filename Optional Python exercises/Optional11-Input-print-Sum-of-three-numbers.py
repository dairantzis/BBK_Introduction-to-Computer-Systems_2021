

# This program reads two numbers and prints their sum:
a = int(input('Please provide the first number:'))
b = int(input('Please provide the second number:'))
print('The sum of the first two numbers is:',end='')        # The end method defines how the line will be terminated, overriding the default nl
print(a + b)                                                # The sum is calculated and printed within the same statement

# Can you change it so it can read and sum three numbers?

c = int(input('Please provide the third number:'))

print('The sum of the three numbers is:',end='')             # The end method defines how the line will be terminated, overriding the default nl
print(a + b + c)
