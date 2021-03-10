#
# A cupcake costs A dollars and B cents. Determine, how many
#   dollars and cents should one pay for N cupcakes.  A program
#   gets three numbers: A, B, N. It should print two numbers:
#   total cost in dollars and cents.
#
dollarsCost = int(input('What is the dollar cost of a cupcake?'))
centsCost = int(input('What is the cents cost of a cupcake?'))
numberOfCupcakes = int(input('How many cupcakes do you want to buy?'))

# calculate the total cost in cents
totalCostInCents = numberOfCupcakes * (dollarsCost * 100 + centsCost)

# print the result in dollars and cents by using division and modulo
print('Total cost is:',totalCostInCents // 100,'dollars and',totalCostInCents % 100,'cents.')



