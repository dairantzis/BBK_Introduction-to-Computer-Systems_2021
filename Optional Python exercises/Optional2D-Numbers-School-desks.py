#
# A school decided to replace the desks in three classrooms. Each desk sits
#   two students. Given the number of students in each class, print the smallest
#   possible number of desks that can be purchased.
#
# The program should read three integers: the number of students in each of the three
#   classes, `a`, `b` and `c` respectively.
#
# In the first test there are three groups. The first group has 20 students and thus needs 10 desks.
# The second group has 21 students, so they can get by with no fewer than 11 desks.
# 11 desks is also enough for the third group of 22 students. So we need 32 desks in total.
#
import math

studentsInClassA = int(input('How many students are in class A?'))
studentsInClassB = int(input('How many students are in class B?'))
studentsInClassC = int(input('How many students are in class C?'))

desksNeededForClassA = math.ceil(studentsInClassA / 2)

print('Desks needed for class A:',desksNeededForClassA)

desksNeededForClassB = math.ceil(studentsInClassB / 2)

print('Desks needed for class B:',desksNeededForClassB)

desksNeededForClassC = math.ceil(studentsInClassC / 2)

print('Desks needed for class C:',desksNeededForClassC)

totalDesksNeeded = desksNeededForClassA + desksNeededForClassB + desksNeededForClassC

print('Total desks needed for the school:',totalDesksNeeded)

                       

