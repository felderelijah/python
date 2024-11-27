# wifi diagnostic tree

print('Reboot the computer and try to connect.')

# user input
fix = input('Did that fix the problem? ')

# nested if/else statements for issues not being resolved 
if fix == 'no':
    print('Reboot the router and try to connect.')
    fix = input('Did that fix the problem? ')
    if fix == 'no':
        print('Make sure the cables between the router & \
modem are plugged in firmly.')
        fix = input('Did that fix the problem? ')
        if fix == 'no':
            print('Move the router to a new location \
and try to connect.')
            fix = input('Did that fix the problem? ')
            if fix == 'no':
                print('Get a new router.')
            else:
                print('Issue resolved!')
        else:
            print('Issue resolved!')
    else:
        print('Issue resolved!')
else:
    print('Issue resolved!')
