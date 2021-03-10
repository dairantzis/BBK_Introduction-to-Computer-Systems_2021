#
# Given a square of a chessboard. If it's a black square, print YES, otherwise print NO.
#
# The program receives two integers from 1 to 8 specifying the column and row number of the square.
#
squarex = int(input('Please enter the x coordinate of the square:'))
squarey = int(input('Please enter the y coordinate of the square:'))

print('The square is:',end=' ')
# both numbers are odd, or both numbers are even, then the square is black
if ((squarex % 2 == 1) and (squarey % 2 == 1)) or ((squarex % 2 == 0) and (squarey % 2 == 0)):
    print('black')
else:
    print('white')
    
