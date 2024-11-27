#sum of numbers

#running total
numbers = 0

#use of walrus operator for less lines of code
while (number := float(input('Enter a series of postive numbers: '))) > -1:
    numbers = numbers + number

#results
print(f'\nThe sum is {numbers}.')
