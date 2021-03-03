

# Write a program that reads an integer number
#   and prints its previous and next numbers.

number = int(input('Please enter an integer number:'))  # prompt the user to input an integer

previousNumber = number - 1                             # calculate the numbers before
followingNumber = number + 1                            #  and after the number, before printing all of them.
             
print(str(previousNumber)+', is before '+str(number)+', which is before '+str(followingNumber))