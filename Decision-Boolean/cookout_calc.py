# hot dog cookout calculator

# user input for hotdogs and people
people = int(input('How many people will be at the cookout: '))
dogs = int(input('How many hot dogs will each person get: '))

# constant number of packaged items 
HDPACK = 10
BUNPACK = 8

# calculations
hotdogs = people * dogs
buns = hotdogs

dogPack = hotdogs // HDPACK
bPack = hotdogs // BUNPACK

dogLeft = (dogPack * HDPACK) - hotdogs
bunLeft = (bPack * BUNPACK) - hotdogs
leftDogs = abs(dogLeft) # abs to turn the value into a positive integer
leftBuns = BUNPACK - abs(bunLeft)

# guarantees a minimum of packages for buns and dogs
if dogPack == 0:
    dogPack = 1
    if bPack == 0:
        bPack = 1
    else:
        bPack = bPack
else:
    dogPack = dogPack

# this if statement is to guarantee that there shoud be more package
# buns than dogs 
if dogPack == bPack and hotdogs > 10:
    bPack = dogPack + 1
else:
    bPack = bPack
    
# results

print(f'\nThe minimum number of packages of hot dogs required: {dogPack}')
print(f'The minimum number of packages of hot dogs buns \
required: {bPack}')
print(f'The number of hot dogs that will be left over: {leftDogs}')
print(f'The number of hot dogs buns that will be left over: {leftBuns}')
