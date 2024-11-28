# average of numbers

# Assume a file containing a series of integers is named numbers.txt
# and exists on the computer’s disk.
# Write a program that calculates the average of all the numbers stored in the file.

infile = open('numbers.txt', 'r')
line = infile.readline()

total = 0
entries = 0

while line != '1':
    values = float(line)
    entries += 1
    print(f'{entries}: {values}')
    total += values
    line = infile.readline()
    

infile.close()

print(f'\nThe average is {total / entries:.2f}')
