# for loop used for the upper part of the pattern
for i in range(0, 6):
    for j in range(0, i):
        print('*', end = ' ')
    print('')

# for loop used for the lower part of the pattern
for i in range(4, 0, -1):
    for j in range(0, i):
        print('*', end = ' ')
    print('')
    


