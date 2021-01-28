
print (21, 4*32, 'hello')

x = 31 
print (x, bin(x), hex(x))

y = 0b1011 
z = 0xA3 
print (y, z)

w = x + y + z 
print ('the sum is ', w)

print ('the sum of',x,y,z,'is:', sep = ',',end='')
print(w)
print('this is printed in the following line since the end of the print statement is not modified')
