#
import math
#
# A car can cover distance of N kilometers per day.
#   How many days will it take to cover a route of
#   length M kilometers?
# The program gets two numbers: N and M.
#
kmPerDay = int(input('How many km can the car travel per day?'))
lengthOfRoute = int(input('How long is the route to be covered?'))

# The result of the division is needed to answer this exercise
# round(number, digits)
# In this case, the number will be rounded down if the decimal
#   point of the number <= .5
#   and will be rounded up if the decimal point > 0.5
# Digits indicate the number of digits used in the result.
#
# Another approach is to use the ceil function which returns
#   the smallest integer that is not less than the number provided.
#
Result = lengthOfRoute / kmPerDay

ResultUsingRound = round(lengthOfRoute / kmPerDay,2)

ResultUsingCeil = math.ceil(lengthOfRoute / kmPerDay)

print('Result:',Result)
print('Result using Round:',ResultUsingRound)
print('Result using Ceil:',ResultUsingCeil)
