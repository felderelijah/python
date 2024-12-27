#constants for menu
CREATE = 1
SEARCH = 2
UPDATE = 3
DELETE = 4
EXIT = 5

def main():
    phonebook = {}
    
    choice = 0
    while choice != EXIT: # display options
        choice = displayMenu()

        if choice == CREATE:
            create(phonebook)
        elif choice == SEARCH:
            search(phonebook)
        elif choice == UPDATE:
            update(phonebook)
        elif choice == DELETE:
            delete(phonebook)
        elif choice == EXIT:
            break
        else:
            correction()

    print('\nYour contact list: ')
    if phonebook == {}:
        print('You have no contacts!')
    else:
        for contacts in phonebook:
            print(contacts)


def displayMenu(): # visual menu display option
    print('\n1. Create a new contact' +
          '\n2. Search for a contact' +
          '\n3. Change an existing contact number' +
          '\n4. Delete an existing contact number' +
          '\n5. Exit your contact list')

    choice = int(input('\nWhat would you like to do today: '))
    return choice

def create(phonebook): # new contacts added

    firstName = input('\nWhat is the first name for the contact: ')
    lastName = input('What is the last name for the contact: ')
    fullName = firstName + ' ' + lastName

    if fullName.lower() in phonebook:
        print(f'You already have a contact for {fullName}.')
        while True:
            decision = input('Would you like to update this contact instead (yes or no): ')
            if decision.lower() == 'yes':
                update(phonebook)
                break
            elif decision.lower() == 'no':
                break
            else:
                correction()
    else:
        number = input('What is the phone number for the contact: ')
        phonebook[fullName.lower()] = number

def search(phonebook): # seaching contact list
    who = input('\nWho are you looking for (full name): ')

    print(phonebook.get(who.lower(), 'Not found.'))
    if who.lower() not in phonebook:
        option(who, phonebook)

def update(phonebook): # changing someone contact
    who = input('Who number would you like to change (full name): ')
    if who.lower() in phonebook: 
        number = input('What is their new number: ')
        phonebook[who.lower()] = number
        print(f'{who} contact was updated.')
    if who.lower() not in phonebook:
        print(f'{who} is not in your contact list.')
        option(who, phonebook)
        
def delete(phonebook): # delete someone number
    who = input('What contact would you like to delete (full name): ')

    if who.lower() in phonebook:
        del phonebook[who.lower()]
        print(f'{who} is no longer in your contact list.')
    elif who.lower() not in phonebook:
        print(f'{who} is already not in your contact list.')

def option(who, phonebook): # to add/ignore individuals who didn't appear in contact list
    while True:
            option = input(f'\nWould you like to add {who} to your contacts (yes or no): ')
            if option.lower() == 'yes':
                create(phonebook)
                break
            elif option.lower() == 'no':
                print(f'Okay {who} will not be added right now.')
                break
            else:
                correction()
                
def correction(): # input validation response
    print('Not an option')

if __name__ == '__main__':
    main()
