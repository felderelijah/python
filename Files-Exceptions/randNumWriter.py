# random number file writer

# Write a program that writes a series of random numbers to a file.
# Each random number should be in the range of 1 through 500.
# The application should let the user specify how many random numbers
# the file will hold.

import random

file = open('/Users/elijahfelder/Downloads/CSIT-216/Assignments/Lab 6/randNumFile.txt', 'w')

many = int(input('How many entries would you like to enter: '))

counter = 0

for x in range(many):
    num = random.randint(1, 500)
    numString = str(num)
    counter += 1
    print(f'Number #{counter}: {numString}')
    file.write(f'{numString}\n')

file.close()
