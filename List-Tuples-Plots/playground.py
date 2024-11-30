# linear graph chart

# This was fun exercise to get the understanding of list, tuples, loops, and plots.
# This program is designed to receive input from the user for coordinates suggestions.
# After receiving the suggestions they are stored in a empty list and later displayed.
# Then the two list are represented ina graph based on the X and Y axis.

import matplotlib.pyplot as plt # alias is plt to refer to the import module

def coordin():
    suggest = int(input('How many data points would you like to enter: '))

    # empty list
    xcord = [] 
    ycord = []

    count = 0

    for many in range(suggest):
        count += 1
        xspot = int(input(f'Enter X coordinate #{count}: ')) 
        xcord.append(xspot) # stores input to empty list
        yspot = int(input(f'Enter Y coordinate #{count}: '))
        ycord.append(yspot)
    return xcord, ycord # allows use in other functions

def insertion():
    newspots = coordin() # variable has access to function
    for unique in newspots:
        print(unique)
    return unique

def main():

    plt.plot(insertion()) # alias with the function as the argument

    plt.show() # in order for the graph to show

if __name__ == '__main__':
    main()
