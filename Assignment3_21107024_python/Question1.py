import math
num = float(input("Enter a decimal number which is to be converted into its binary equivalent: "))

#Converting integer part to binary
num_int = math.trunc(num)
list1 = list()

while num_int >= 1:
    a = (num_int % 2)
    list1.append(str(a))
    num_int //= 2

bin_int_str = ''.join(list1)
bin_int = bin_int_str[::-1]

#Converting fractional part to binary
list2 = list()
num_frac = divmod(num, 1)
frac = (num_frac[1])

i = int(input("Precision (No. of decimal places in the answer): "))

ch = 1
while ch <= i:
    k = (frac * 2)
    b = math.trunc(k)
    list2.append(str(b))
    l = divmod(k, 1)
    frac = l[1]
    ch = ch + 1

bin_frac = ''.join(list2)
bin_final = bin_int + '.' + bin_frac
print(float(bin_final))

