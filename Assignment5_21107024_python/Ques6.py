start = int(input("Enter the initial no. of the range:"))
end = int(input("Enter the final no. of the range(not included in the range): "))

for i in range(start, end):
    result = 'prime'
    c = 2
    if (i == 0) or (i == 1):   # 0 and 1 are neither prime nor composite
        print(f"{i} is not prime.")
    else:        
        while c < i:
            if i % c == 0:
                result = 'not prime'   # for composite nos. (divisible by no. other than 1 and the no. itself)
                break                  # to exit the while loop 
            c += 1
        print(f"{i} is {result}.")
