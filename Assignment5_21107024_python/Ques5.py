num_of_rows = int(input("Enter number of rows: "))
count = 0

for i in range(0, num_of_rows):
    for j in range(0, i):
        if count > 25:                  # if statement is used for continuing the pattern after 'Z'
            count = count - 26
        print(chr(65 + count), end = '')
        count += 1
    print()
        