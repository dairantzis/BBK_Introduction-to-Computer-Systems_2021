# variables, names and memory addresses
#
def printValues(a,b,c,d):
    print("The value of a is:",a)
    print("The value of b is:",b)
    print("The value of c is:",c)
    print("The value of d is:",d)
    print()
    
x = 10
print("The value of x is:" ,x, "stored at address: ",id(x),"\n")
x += x + 1
print("Increased the value of x:" ,x, "stored at address: ",id(x),"\n")
x += x - 1
print("Decreased the value of x:" ,x, "stored at address: ",id(x),"\n")
y = x
print("Assigned the value of x to y.  x is stored at address:",id(x),"and y is stored at address:",id(y),"\n")


# A pointer can be used to pass a list as parameter to a function call
listVariable = [1, 2, 3, 4.4]
print("Variable listVariable is stored at address:",id(listVariable),"\n")
printValues(*listVariable)

# A pointer can be used to pass a tuple as parameter to a function call
tupleVariable = (5,6.5,7,8.4)
print("Variable tupleVariable is stored at address:",id(tupleVariable),"\n")
printValues(*tupleVariable)

# A pointer can be used to pass a dictionary as parameter to a function call
mappedVariable = {'a': 115, 'c' : 789.6, 'b' : 456, 'd' : 123}
print("Variable mappedVariable is stored at address:",id(mappedVariable),"\n")
printValues(**mappedVariable)

# A pointer can be used to pass a set as parameter to a function call
setVariable = {'red',5,7.8,'blue'}
print("Variable setVariable is stored at address:",id(setVariable),"\n")
printValues(*setVariable)
