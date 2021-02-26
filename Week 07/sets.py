
# define a set by using curly brackets.  The elements will be placed as is
setVariable = {'red',5,7.8,'blue'}
setVariable2= {'red','green','yellow'}

# all the contents can be printed in one statement:
print(setVariable)

# define a set by using the set() method.  A list of elements to be included in the set is generated.
setVariable1 = set('blue')
print(setVariable1)

# an empty set can only be defined by using the set() method because {} are also used in dictionaries.
setEmpty = set()
print(setEmpty)

# the length of the set can be queried
print('The length of setVariable is:',len(setVariable))

# items can be added to a set
setVariable.add('yellow')
print(setVariable)

# the union of two sets can be calculated
print('setVariable is:',setVariable)
print('setVariable2 is:',setVariable2)
unionSet = setVariable.union(setVariable2)
print('Their union is:',unionSet)

intersectionSet = setVariable.intersection(setVariable2)
print('Their intersection is:',intersectionSet)

differenceSet = setVariable.difference(setVariable2)
print('Their difference is:',differenceSet)



