ch = 'y'
while ch == 'y':
    year = int(input("Enter a year: "))
    if year % 4 == 0:
        if (year % 100 == 0) & (year % 400 == 0):
            print(f"{year} is a leap year.")
        elif (year % 100 == 0) & (year % 400 != 0):
            print(f"{year} is not a leap year.")
        else:
            print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")
    ch = input("Do you want to continue? (Enter y for yes and n (or any key other than y) for no)")
