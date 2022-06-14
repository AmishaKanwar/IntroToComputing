str_input = input("Enter string to be reversed:")
str_reverse = ""

for i in str_input:
    str_reverse = i + str_reverse     # elements will be added from the left in the empty string (concatenation)

print("The reversed string is:", str_reverse, sep = "\n")