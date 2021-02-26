# Birkbeck, Introduction to computer systems module
# Python training programme based on week 3 quiz worksheet
#
# This program calculates the percent of compression given the formula:  
# Percent of compression = (Compressed Text Size + Dictionary size) divided 
# by original size, subtracted from 100%
#
# The original text size is 240 characters, the compressed text size  
# is 148 characters, and the dictionary size is 25 characters.
#
originalSize = 240         # initialise the variables 
dictionarySize = 25
compressedSize = 148

compressionPercentage = 1 - ((compressedSize + dictionarySize) / originalSize)   # calculate the compression ratio

# present the result to the user
print('  Compressed text size: ',compressedSize,' characters',sep = '')
print('       Dictionary size: ',dictionarySize,' characters',sep = '')
print('                 Total: ',compressedSize+dictionarySize,' characters',sep = '')
print('    Original text size: ',originalSize,' characters',sep = '')
print('Compression percentage: {:.2%}'.format(compressionPercentage))  # format the output to 2 decimal places, percentage

