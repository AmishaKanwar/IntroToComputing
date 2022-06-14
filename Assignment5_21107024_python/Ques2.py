num = int(input("Enter the no. by which divisibility is to be checked: "))
start = int(input("Enter the lower limit of the range in which divisibility is to be checked: "))
end = int(input("Enter the upper limit (excluded) of the range in which divisibility is to be checked: "))

for i in range(start, end):
    if i % num == 0:        # if the remainder obtained is 0, then the no. is divisible by the given digit.
        print(i)
print(f"These are the numbers divisible by {num} in the range (0, {end}) [{end} not included].")