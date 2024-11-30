digits = [] # empty list

SERIES = 20 # series of 20 numbers 
total = 0.0 # running total

for numbers in range(SERIES):
    value = float(input("Enter a number: "))
    digits.append(value) # adds input to list
total = sum(digits)
average = total / len(digits)

# high and low values
highest = max(digits) 
lowest = min(digits) 

print(f'\nThe lowest number in the list is {lowest:.2f} \
\nThe highest number in the list is {highest:.2f} \nThe sum total \
of the list is {total:.2f}. \nThe average of the \
list is {average:.2f}.')


