# importing "array" for array creations 
#import array as arr 
import array
 
# create an array with integer type
# the letter i instructs the interpeter that
# the contents of the array are integers.
# Other possible options are:
# b, B, u, h, H, i, I, l, L, q, Q, f, d
a = array.array('i', [1, 2, 3, 5, 8, 15]) 
  
# accessing the array 
print ("The array contents are : ", end =" ") 
for i in range (0, 3): 
    print (a[i], end =" ") 
print()

# to insert an element into the array  
# for example insert 4 at index location 1,
# use the insert() function 
a.insert(1, 4) 

# accessing the array
print ("The array contents are : ", end =" ") 
for i in (a): 
    print (i, end =" ") 
print()

# adding an element using append() 
a.append(67) 
  
print ("The array contents are : ", end =" ") 
for i in (a): 
    print (i, end =" ") 
print()

# work with elements within a range 
withinRange = a[3:5] 
print("The elements in the range 3 to 5 (not included) are: ") 
print(withinRange) 
  
# work with elements from a point till the end 
tillTheEnd = a[5:] 
print("The elements from the 5th element till the end are: ") 
print(tillTheEnd) 
  
# work with the first 5 elements 
fromTheBeginning = a[:5] 
print("The first 5 elements are: ") 
print(fromTheBeginning)

# removing an element at index 2 
print ("The popped element is : ", end ="") 
print (a.pop(2))







