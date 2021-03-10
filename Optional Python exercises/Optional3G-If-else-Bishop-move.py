#
# Chess bishop moves diagonally in any number of squares.
# Given two different squares of the chessboard, determine
#   whether a bishop can go from the first square to the
#   second one in a single move.
#
# The program receives four numbers from 1 to 8 each specifying
#   the column and the row number, first two - for the first
#   square, and the last two - for the second square. The program
#   should output YES if a bishop can go from the first square to
#   the second one in a single move or NO otherwise.
#
squarex1 = int(input('Please enter the x coordinate of the first square:'))
squarey1 = int(input('Please enter the y coordinate of the first square:'))

squarex2 = int(input('Please enter the x coordinate of the second square:'))
squarey2 = int(input('Please enter the y coordinate of the second square:'))

#
# Since the bishop can move only diagonally, the change in the value of both the
#   square coordinates must not be 0 in any direction.
#   Also, the magnitude of the change must be equal in both axes.
#   Calculate the relative change of the coordinates and accept the move
#   only if the change is not equal to 0 in both axes and the change
#   in one axis is equal to the change of the other.
#

# Calculate the change in both directions
deltaX = abs(squarex1 - squarex2)
deltaY = abs(squarey1 - squarey2)

# print(deltaX)
# print(deltaY)

# check whether both of the changes are not equal to zero
if (deltaX != 0) and (deltaY != 0) and (deltaX == deltaY):
    print('YES')
else:
    print('NO')
