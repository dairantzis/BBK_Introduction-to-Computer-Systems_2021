# Programme to demonstrate the use of recursion
# A series of numbers is converted to their binary and hexadecimal equivalents and are printed
# The programme was adapted from an initial approach presented by Xu Han in the tutorial of 21/1/2021

def getDecToBin(number,binString):
    bitChar = ''                                       # initialise the string that will carry the current bit
    print('On entry number is: ',number,'/ binString is:',binString,'.',sep='')
    if number>1:                                       # base case: number = 1
        if number%2 == 0:                              # test whether the number is even
            bitChar = '0'                              # if even, add a 0 to the binString
        else:
            bitChar = '1'                              # if odd, add a 1 to the binString
            number = number - 1                        # turn the number into an odd one
        binString = getDecToBin(number//2,binString)   # the function is called again after dividing the number by 2, ready to calculate the next bit
    else:
        bitChar = '1'                                  # base case: number = 1
    binString += bitChar                               # append the current bit character to the existing binString
    print('On  exit number is: ',number,'/ binString is:',binString,'.',sep='')
    return (binString)                                 # return the current binString to the caller, it might be appended upon return there

def hexDigit(x):
    if x < 10:
        return str(x)
    elif (x == 10):
        return 'a'
    elif (x == 11):
        return 'b'
    elif (x == 12):
        return 'c'
    elif (x == 13):
        return 'd'
    elif (x == 14):
        return 'e'
    elif (x == 15):
        return 'f'

def getDecToHex(number,hexString):
    nibbleChar = ''                                    # initialise the string that will carry the current nibble
    print('On entry number is: ',number,'/ hexString is:',hexString,'.',sep='')
    if number > 15:                                    # base case: number <= 15
        nibbleChar = hexDigit(number%16)               # the current nibble is extracted by calculating the modulo 16 of the number
        hexString = getDecToHex(number//16,hexString)  # the function is called again after dividing the number by 16, ready to calculate the next nibble
    else:
        nibbleChar = hexDigit(number)                  # base case reached: the number <= 15
    hexString += nibbleChar                            # append the current nibble character to the existing hexString
    print('On  exit number is: ',number,'/ hexString is:',hexString,'.',sep='')
    return (hexString)                                 # return the current hexString to the caller, it might be appended upon return there


n = 30                                                 # initialise the loop control variable to 30
while n >= 30 and n <= 33:                             # repeat the loop for as long as n >= 30 and n <= 33
    print('Forming the binary number string...')
    binString = ''                                     # prepare an empty string to host the result of the decimal to binary conversion
    binString = getDecToBin(n,binString)               # call getDecToBin to form binString recursively
    print()
    print('Forming the hexadecimal number string...')
    hexString = ''
    hexString = getDecToHex(n,hexString)               # call getDecToHex to form hexString recursively
    print()                                            # print an empty line to separate the result from the demostration comments
    print(n,'\t0b',binString,'\t0x',hexString, sep='')   # print the number in decimal, followed by the binary and hex equivalent
    print()                                            # print an empty line to separate the results of each conversion
    n += 1                                             # increase the loop control variable by one and repeat the loop for the remaining numbers
    