rainFall = [] # empty list

YEAR = 12 # how many months in a year
totalRain = 0.0 # running total

for month in range(YEAR):
    rain = float(input(f"Enter the total ranifall for month #{month+1}: "))
    # add 1 to month so the index can correlate with the the actual
    # calendar year
    rainFall.append(rain) # adds input to list
totalRain = sum(rainFall)
averageRain = totalRain / len(rainFall)

calendarMonths = ['January', 'February', 'March', 'April', 'May',
                  'June', 'July', 'August', 'September', 'October',
                  'November', 'December'] # list position corresponds w/ rainFall

highestMonth = rainFall.index(max(rainFall)) #large precipitation
lowestMonth = rainFall.index(min(rainFall)) #least precipitation

print(f'\nThe total amount of rainfall for the year is {totalRain:.2f} \
\nThe average monthly rainfall is {averageRain:.2f} \nThe month with \
the highest amounts of rain is {calendarMonths[highestMonth]}. \nThe month with the lowest \
amounts of rain is {calendarMonths[lowestMonth]}.')

