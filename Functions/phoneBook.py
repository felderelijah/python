# add phone numbers

def phoneBook():                     
    addMore = 'y'
    while addMore == 'y':
        name = input('Who phone number would you like to add: ')
        number = input(f'Okay, enter {name} number: ')

        while len(number) < 10: #validating phone number input
            print('\nPhone numbers are at least 10 single digits')
            number = input(f'Okay, enter {name} number: ')

        print(f'\n{name}: {number}') # display associated input

        addMore = input('\nWould you like to another phone number: ')
        
        if addMore != 'y':
            break #exits the loop if user chooses not to add another 

phoneBook()
    
