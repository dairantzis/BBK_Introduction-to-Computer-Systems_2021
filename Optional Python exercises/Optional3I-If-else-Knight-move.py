#
# Chess knight can move to a square that is two squares
#   away horizontally and one square vertically, or two
#   squares vertically and one square horizontally. The
#   complete move therefore looks like the letter _L_.
#   Given two different squares of the chessboard, determine
#   whether a knight can go from the first square to the
#   second one in a single move.
#
# The program receives four numbers from 1 to 8 each
#   specifying the column and the row number, first two -
#   for the first square, and the last two - for the second
#   square. The program should output YES if a knight can go
#   from the first square to the second one in a single move
#   or NO otherwise.
#
squarex1 = int(input('Please enter the x coordinate of the first square:'))
squarey1 = int(input('Please enter the y coordinate of the first square:'))

squarex2 = int(input('Please enter the x coordinate of the second square:'))
squarey2 = int(input('Please enter the y coordinate of the second square:'))

#
# Since the knight can move in a combination of two squares in one direction,
#   followed by one square at another, horizontal and vertical movements
#   will exhibit either deltaX, or deltaY equal to 2 in one direction and
#   equal to 1 in the other.
#   Calculate the relative change of the coordinates and accept the move
#   only if the above options are true.
#

# Calculate the change in both directions
deltaX = abs(squarex1 - squarex2)
deltaY = abs(squarey1 - squarey2)

#print(deltaX)
#print(deltaY)

if ((deltaX == 2) and (deltaY == 1)) or ((deltaX == 1) and (deltaY == 2)):
    print('YES')
else:
    print('NO')

