#
# Given a two-digit integer, print its left digit
#   (a tens digit) and then its right digit (a ones
#   digit). Use the operator of integer division to
#   obtain the tens digit and the operator of taking
#   the remainder to obtain the ones digit.
#

number = int(input('Please enter a two digit integer:'))

decades = number // 10      # use floor division to obtain the decades
units = number % 10         # use modulo to obtain the units

# formulate a message to return to the user
outputMessage = 'There are ' + str(decades) + ' decades and ' + str(units) + ' units in ' + str(number)
print(outputMessage)

