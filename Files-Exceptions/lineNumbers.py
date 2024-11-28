# line numbers

# Write a program that asks the user for the name of a file.
# The program should display the contents of the file with each line
# preceded with a line number followed by a colon.
# The line numbering should start at 1.

file = input('Enter the name of the file with extension\n Example - (hello.txt): ')

program = open(file, 'r')

lineNumber = 0

print('Winners')
for x in program:
    lineNumber += 1
    print(f'{lineNumber}: {x}')

program.close()
