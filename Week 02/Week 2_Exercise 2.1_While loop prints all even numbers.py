# Example of while loop
# The user is asked to input an upper and a lower limit
#   and the programme then prints the even numbers between them
# No input error checking is done

lowerLimit = int(input('Please, enter the lower limit integer:'))
upperLimit = int(input('Please, enter the upper limit integer:'))

print('The even numbers between', lowerLimit, 'and' ,upperLimit, 'are:')

number = lowerLimit                # the loop control variable is initialised to the lower limit

while(number < upperLimit):        # the loop will be repeated while number remains < upperLimit
    if number%2 == 0:              # modulo 2 is used to test whether the current number is odd/even 
        print(number,' ',end = '') # if the number is even, then it is printed
    number = number + 1            # number, the loop control variable, is increased by one, ready for the next iteration
    


