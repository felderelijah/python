# test average and grade

x = 5 # loop counter

def calc_average():
    print('Enter the five test scores below.')
    exams = 0 #running total for the number to be displayed for which exam was taken
    testTotal = 0 # running total
    for b in range(x):
        test = float(input('\nEnter the test score: '))
        exams += 1
        print(f'Exam #{exams} you entered: {test}')
        testTotal = testTotal + test
    average = testTotal/x
    print(f'\nYour test score calculated to {testTotal} and your average is {average}%\n')
    

def determine_grade():
    keepGoing = 'y'
    while keepGoing == 'y':
        testScore = float(input('\nEnter a test score: '))
        if testScore >= 90:
            print('You received an A.')
        elif testScore >= 80 and testScore <= 89:
            print('You received an B.')
        elif testScore >= 70 and testScore <= 79:
            print('You received an C.')
        elif testScore >= 60 and testScore <= 69:
            print('You received an D.')
        elif testScore < 60:
            print('You received an F.')
        keepGoing = input('\nEnter y to keep going or any to key to stop: ') # to avoid a infinite loop 
        if keepGoing != 'y':
            break
        
    print('Your Done.')


calc_average()
determine_grade()

