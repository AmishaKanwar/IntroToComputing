print("Following are the numbers divisible by 7 and 11 in the range 1 - 500")
for i in range(0, 500):        # for loop used to check divisibilty of numbers in a range by certain digits
    if (i % 7 == 0) and (i % 11 == 0):
        print(i)