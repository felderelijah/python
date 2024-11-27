# distance traveled

# formula for distance = speed * time

speed = int(input('The speed of the vehicle \
(in miles per hour): ')) #user input

#validation input to avoid negative integer input
while speed < 0:
        print('Error: MPH cannot be a negative number. Try again.')
        speed = int(input('The speed of the vehicle \
(in miles per hour): '))
        
time = int(input('\nThe number of hours it \
has traveled: '))

#validation input to avoid negative integer input
while time < 0:
        print('Error: Time traveled cannot be a negative number. Try again.')
        time = int(input('The number of hours it \
has traveled: '))

print("\nHour \tDistance Traveled \
\n-------------------------")

for hour in range(1, time + 1):
    distance = speed * hour
    print(f'{hour} \t{distance}')
