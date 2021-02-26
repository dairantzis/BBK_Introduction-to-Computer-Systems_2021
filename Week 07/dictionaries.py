
# assume a dictionary holding the parameters of a serial port
setupDictionary = {'ComPort' : '-com1','ComSpeed' : '115200', 'FlowControl' : 'no'}

# all the contents can be printed in one statement:
print(setupDictionary)

# the existence of a key can be tested
print('ComPort' in setupDictionary)
print('FlowControlType'in setupDictionary)

# the value of a key pair can be altered
setupDictionary['ComSpeed'] = '9600'
print(setupDictionary)

# a new key value pair can be added
setupDictionary['FlowControlType'] = 'RTS/CTS'
setupDictionary['IdleTime'] = '100 msec'
print(setupDictionary)

# a key value pair can be removed
setupDictionary.pop('IdleTime')
print(setupDictionary)

# all key value pairs can be printed with a for loop
for n, m in setupDictionary.items():
    print(n,m)
    
# finally, a dictionary can be cleared
setupDictionary.clear()
print(setupDictionary)

