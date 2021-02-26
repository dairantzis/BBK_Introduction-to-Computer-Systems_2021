# The programme uses a while loop to apply the Euclidean algorithm
#   to calculate the greates common denominator of two integers
# The algorithm provided is:
# X ←  the larger input;
# Y ←  the smaller input;
# while (Y not zero) do
#  (Remainder ←  remainder after dividing X by Y;
#  X ←  Y;
#  Y ←  Remainder);
# GCD ←  X
# Test cases are: 252,105 GCD:21 and 60,50 gcd:10
#

def GCD(X,Y):
    while (Y!= 0):              # Repeat the loop for as long as Y is not 0
        Remainder = X%Y         # Use the modulo function to calculate the remainder
        X = Y                   # rotate the values in the variables
        Y = Remainder
    return(X)

X = int(input('Please, enter the larger integer:'))
Y = int(input('Please, enter the smaller integer:'))
print(GCD(X,Y))


