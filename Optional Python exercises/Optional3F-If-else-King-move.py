#
# Chess king moves one square in any direction. Given two different
#   squares of the chessboard, determine whether a king can go from
#   the first square to the second one in a single move.
#
# The program receives four numbers from 1 to 8 each specifying the
#   column and the row number, first two - for the first square, and
#   the last two - for the second square. The program should output
#   YES if a king can go from the first square to the second one in
#   a single move or NO otherwise.
#
squarex1 = int(input('Please enter the x coordinate of the first square:'))
squarey1 = int(input('Please enter the y coordinate of the first square:'))

squarex2 = int(input('Please enter the x coordinate of the second square:'))
squarey2 = int(input('Please enter the y coordinate of the second square:'))

#
# Since the king can move only one square, the change in the value of the
#   square coordinates must not exceed 1 at any direction.
#   Calculate the relative change of the coordinates and accept the move
#   only if the change in both axes <= 1 and not equal to 0 in both axes.
#

# Calculate the change in both directions
deltaX = abs(squarex1 - squarex2)
deltaY = abs(squarey1 - squarey2)

# print(deltaX)
# print(deltaY)

# check whether either of the changes is not equal to zero
if (deltaX != 0) or (deltaY != 0):
    if (deltaX <= 1) and (deltaY <= 1):           # check whether the move <= 1 square
        print('YES')
    else:
        print('NO')
else:
    print('The king remains at the same square!') # no change in either direction - let the user know
