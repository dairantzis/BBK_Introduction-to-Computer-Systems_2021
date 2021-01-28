# Programme to calculate and print the factors of an integer number provided by the user
# The factors of a number are numbers which, when multiplied together, result to the number.
# In other words, the factors are the divisors of the number.
#
# Since the factors divide the number, the remainder of their division of the number is 0.
# The modulo function is used to find them.
#

number = int(input('Please, enter a positive integer:'))

n = 1                                    # n will be the control variable of the loop

print('The factors of ',number,' are: ',sep = '', end = '')

while n < number:                        # repeat the loop while n < number (a number is divisible by itself)
    if number % n == 0:                  # if number modulo n is zero, then n divides the number
        print(n,',',sep = '',end = '')   # print the number
    n = n + 1                            # increase the number by one and repeat the loop

print(n)                                 # print the number itself as a number is divisible by itself
