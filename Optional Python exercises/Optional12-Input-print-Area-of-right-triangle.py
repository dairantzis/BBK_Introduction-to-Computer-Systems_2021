# Statement

# Write a program that reads the length of the base and
#   the height of a right-angled triangle and prints the area.
#   Every number is given on a separate line.

import math         # import math to make the exercise a bit more interesting.

# Read the numbers b and h like this:
base = int(input('Please provide the base of the right-angled triangle:'))
height = int(input('Please provide the height of the right-angled triangle:'))

# Print the result with print()
area = base * height / 2

print('The area of the triangle is:',area)

# while we are at it, let's calculate other useful things:
# like the hypotenuse
hypotenuse = math.sqrt(base**2 + height**2)
print('The hypotenuse is: {:.2f}'.format(hypotenuse))

# and the altitude
altitude = base * height / hypotenuse
print('The altitude is: {:.2f}'.format(altitude))

 