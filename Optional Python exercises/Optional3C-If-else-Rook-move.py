#
# Chess rook moves horizontally or vertically. Given two different squares
#   of the chessboard, determine whether a rook can go from the first square
#   to the second one in a single move.
#
# The program receives four numbers from 1 to 8 each specifying the column
#   and the row number, first two - for the first square, and the last two
#   - for the second square. The program should output `YES` if a rook can
#   go from the first square to the second one in a single move or `NO` otherwise.
#
square1x = int(input('Please enter the x coordinate of the first square:'))
square1y = int(input('Please enter the y coordinate of the first square:'))

square2x = int(input('Please enter the x coordinate of the second square:'))
square2y = int(input('Please enter the y coordinate of the second square:'))

# Since the rook can only move horizontally, or vertically, either the x coordinates
#   are equal, or the y coordinates are equal

if (square1x == square2x) or (square1y == square2y):
    print('Yes')
else:
    print('No')
    
