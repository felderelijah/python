# Loop pattern

NUMSTEPS = 6 #constant for number of loops


for r in range(NUMSTEPS):
    print('#', end='')
    for b in range(r):
        print(' ', end='') #creates space between the nested loop each rep
    print('#')
