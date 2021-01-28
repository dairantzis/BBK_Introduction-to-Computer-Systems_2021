def getDecToBin(number):
    if number>1:
        getDecToBin(number//2)
    print(number % 2,end = '')

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

def getDecToHex(number):
    if number > 15:
        getDecToHex(number//16)
    print(hexDigit(number%16), end='')

n = 10
while n >= 10 and n <=100:
    print(n, '\t0b', end='')  # Added a tab to improve display
    getDecToBin(n)
    print('\t0x', end='')     # Added a tab to improve display
    getDecToHex(n)
    print()
    n += 1