# exception handling

# Modify the program that you wrote for Exercise 6
# so it handles the following exceptions:
# It should handle any IOError exceptions
# that are raised when the file is opened and data is read from it.
# It should handle any ValueError exceptions that are raised
# when the items that are read from the file are not converted to a number.

try:
    infile = open('numbers-copy.txt', 'r')
    line = infile.readline()

    total = 0
    entries = 0

    while line != '0':
        values = float(line.strip())
        entries += 1
        print(f'{entries}: {values}')
        total += values
        line = infile.readline()
    
    infile.close()

except ValueError:
    print('>>> Can\'t convert to number.')
except Exception as err:
    print(f'>>> An error has occurred: {err}')
else:
    print(f'\nThe average is {total / entries:.2f}')
