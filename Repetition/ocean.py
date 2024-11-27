#ocean levels

newLevel = 0 #running total
RISING = 1.6
QC = 25 #quarter century

for rise in range(1, QC + 1):
    #the index will start at 1
    #in order to display the progession from year 1
    #QC + 1 will stop at year 25 instead pf year 24
    newLevel = newLevel + RISING
    print(f'Year {rise}, the ocean will rise {newLevel:.1f} millimeters')
print(f'\nThe ocean sea level will have a increase of {newLevel:.1f} \
millimetes in 25 years.')
