# restaurant selector

vegetarian = input('Is anyone in your party a vegetarian? ')
vegan = input('Is anyone in your party a vegan? ')
gluten = input('Is anyone in your party gluten-free? ')

if vegetarian == 'no' and vegan == 'no' and gluten == 'no':
    print('Here are your restaurant choices:')
    print("\tJoe’s Gourmet Burgers")
elif vegetarian == 'yes' and vegan == 'no' and gluten == 'no':
    print('Here are your restaurant choices:')
    print("\tMama’s Fine Italian")
elif vegetarian == 'yes' and vegan == 'yes' and gluten == 'no':
    print('Here are your restaurant choices:')
    print('\tMain Street Pizza Company')
else:    
    print('Here are your restaurant choices: ')
    print('\tThe Chef’s Kitchen')
    print('\tCorner Cafe')
