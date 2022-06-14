list_of_num = list()
for i in range(1, 11):
    list_of_num.append(int(input(f"Enter {i}th number: ")))

ch = 'y'             # variable to indicate choice 
while ch == 'y':     # variable empolyed in while loop to perform multiple operations by choice
    print("Press the given numeric keys for the respective operation:")
    print("1 for displaying positive numbers\n2 for displaying negative numbers\n3 for displaying even numbers\n4 for displaying odd numbers")
    print("5 for displaying the number of occurrences of each number")
    choice_op = int(input("Press the key corresponding to the desired operation: "))

    if choice_op == 1:
        print("Positive numbers:")
        for j in list_of_num:
            if j > 0:
                print(j)

    elif choice_op == 2:
        print("Negative numbers:")
        for j in list_of_num:
            if j < 0:
                print(j)

    elif choice_op == 3:
        print("Even numbers:")
        for j in list_of_num:
            if j % 2 == 0:
                print(j)

    elif choice_op == 4:
        print("Odd numbers:")
        for j in list_of_num:
            if j % 2 != 0:
                print(j)

    elif choice_op == 5:
        print("Number of occurrences of each integer:")
        dict1 = dict()
        for j in list_of_num:
            if j not in dict1: 
                dict1[j] = 1
            else:
                dict1[j] += 1
        print(dict1)

    ch = input("Do you want to perform another operation on the given numbers? Press y for yes.")