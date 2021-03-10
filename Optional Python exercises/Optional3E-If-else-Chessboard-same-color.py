#
# Given two squares of a chessboard. If they are painted in the same color,
#   print `YES`, otherwise print `NO`.
# The program receives four integers from 1 to 8, each specifying the column
#   and row number, first two - for the first square, and then the last two -
#   for the second square.
#
squarex1 = int(input('Please enter the x coordinate of the first square:'))
squarey1 = int(input('Please enter the y coordinate of the first square:'))

squarex2 = int(input('Please enter the x coordinate of the second square:'))
squarey2 = int(input('Please enter the y coordinate of the second square:'))

print()
print('The first square is:',end=' ')
# both numbers are odd, or both numbers are even, then the square is black
if ((squarex1 % 2 == 1) and (squarey1 % 2 == 1)) or ((squarex1 % 2 == 0) and (squarey1 % 2 == 0)):
    colourOfFirstSquare = 'black'
else:
    colourOfFirstSquare = 'white'
    
print(colourOfFirstSquare)
print()

print('The second square is:',end=' ')
# both numbers are odd, or both numbers are even, then the square is black
if ((squarex2 % 2 == 1) and (squarey2 % 2 == 1)) or ((squarex2 % 2 == 0) and (squarey2 % 2 == 0)):
    colourOfSecondSquare = 'black'
else:
    colourOfSecondSquare = 'white'
    
print(colourOfSecondSquare)
print()
if colourOfFirstSquare == colourOfSecondSquare:
    print('YES')
else:
    print('NO')



 

