# List initialisation



list1 = [0 for i in range(15)]
list2 = [1, 2, 3]
list3 = ["a", "b", "c", "d", "b", "g"]

print("List 1:",list1)
print("List 2:",list2)
print("List 3:",list3)

list1[0:10] = [10] * 10

print("Ammended the first ten values of List 1:",list1)

list1.extend(list3)

print("Extended list1 with the items in list3:",list1)
print("Note the difference in the nature of the elements")

list1.insert(5,'a')
print("Inserted an a at the first location FOLLOWING element 5:",list1)

list1.remove('a')
print("Removed THE FIRST OCCURENCE of a from the list:",list1)

list1.pop(16)
print("Removed the element immediately FOLLOWING the specified position:",list1)

list1.clear()
print("Cleared list1:",list1)

print("Switching to using list3:",list3)
print("The FIRST occurence of the letter b is at position:",list3.index("b"))
print("Letter b appears within list3:",list3.count("b"),"times.")

list3.sort()
print("Sorted list 3:",list3)

list3.reverse()
print("Reveresed list 3:",list3)

list4 = list3.copy()
print("Copied the contents of list3 onto list4:")
print("This is list3:",list3)
print("This is list4:",list4)

print("End of demonstration of list methods offered by Python")







print(list1)


