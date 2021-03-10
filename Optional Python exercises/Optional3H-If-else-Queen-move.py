#
# Chess queen moves horizontally, vertically or diagonally
#   in any number of squares. Given two different squares of
#   the chessboard, determine whether a queen can go from the
#   first square to the second one in a single move. 
#
# The program receives four numbers from 1 to 8 each specifying
#   the column and the row number, first two - for the first
#   square, and the last two - for the second square. The program
#   should output YES if a queen can go from the first square to
#   the second one in a single move or NO otherwise.
squarex1 = int(input('Please enter the x coordinate of the first square:'))
squarey1 = int(input('Please enter the y coordinate of the first square:'))

squarex2 = int(input('Please enter the x coordinate of the second square:'))
squarey2 = int(input('Please enter the y coordinate of the second square:'))

#
# Since the queen can move in any way she needs to, the direction of
#   the movement must be verified.  Horizontal and vertical movements
#   will exhibit either deltaX, or deltaY equal to 0, but not both,
#   and diagonal movement must exhibit a magnitude of change that is
#   be equal in both axes.
#   Calculate the relative change of the coordinates and accept the move
#   only if the above options are true.
#

# Calculate the change in both directions
deltaX = abs(squarex1 - squarex2)
deltaY = abs(squarey1 - squarey2)

# print(deltaX)
# print(deltaY)

# check whether both of the changes is not equal to zero
if ((deltaX == 0) and (deltaY != 0)) or ((deltaX != 0) and (deltaY == 0)) or (deltaX == deltaY):
    print('YES')
else:
    print('NO')

 