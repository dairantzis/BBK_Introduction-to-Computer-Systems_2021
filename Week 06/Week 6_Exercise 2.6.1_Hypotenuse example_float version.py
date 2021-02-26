# Calculates the hypotenuse of a right triangle
import math

# Inputting the side lengths, with integer conversion
sideA = float(input('Length of side A? '))
sideB = float(input('Length of side B? '))

# Calculate third side via Pythagorean Theorem
hypotenuse = math.sqrt(sideA**2 + sideB**2)

print(hypotenuse)
