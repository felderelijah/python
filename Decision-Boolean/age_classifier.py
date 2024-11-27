# age classifier

# user input only accept whole numbers and not real numbers for exact age
age = int(input('Enter age: '))

# determines a person age classification based off range
if age <= 1:
    print('They are an infant.')
elif age > 1 and age < 13: # both have to be true for accuracy 
    print('They are a child.')
elif age == 13 or age < 20:
    print('They are a teenager.')
else: # any whole number above 19 will be consider an adult 
    print('They are an adult.')
