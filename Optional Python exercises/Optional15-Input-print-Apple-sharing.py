

# N students take K apples and distribute them among each other evenly.
#   The remaining (the indivisible) part remains in the basket. How many
#   apples will each single student get? How many apples will remain in
#   the basket?
#
# The program reads the numbers N and K. It should print the two answers
#   for the questions above.
#

students = int(input('How many students are there?'))
apples = int(input('How many apples will be distributed?'))

applesPerStudent = apples // students  # floor division is used to calculate whole apples per student
applesRemaining = apples % students    # modulo is used to calculate the remaining apples after the distribution

# print the result in a nice, verbose, way
print('Each student will receive '+str(applesPerStudent)+' and there will be '+str(applesRemaining)+' apples left.')
