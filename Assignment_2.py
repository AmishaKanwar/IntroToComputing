#Q1
str1 = "Python is a case sensitive language."
print(len(str1), str1[::-1], sep = '\n')
str2 = str1[slice(10, 26)]
print(str2)
print(str2.replace("a case sensitive", "object oriented"))
print(str1.find('a'))
print(str1.replace(' ', ''))


#Q2
name = 'Amisha'
sid = 21107024
dept_name = 'Mechanical'
cgpa = 9.55
print(f"Hey, {name} here!\nMy SID is {sid}\nI am from {dept_name} department and my CGPA is {cgpa}")


#Q3
a = 56
b = 10
print(a & b, a | b, a ^ b)
print(a << 2, b << 2)
print(a >> 2, b >> 4)


#Q4
str_input = input("Enter any alphanummeric text (symbols can be included):")
if 'name' in str_input:
    print("Yes")
else:
    print("No")


#Q5
a = int(input("Enter the length of 1st side of a triangle:"))
b = int(input("Enter the length of 2nd side of a triangle:"))
c = int(input("Enter the length of 3rd side of a triangle:"))
end_result = (a>=(b+c)) | (b>=(a+c)) | (c>=(a+b)) == 1
print(str(end_result).replace('True', 'No').replace('False', 'Yes'))


#Q6
a = int(input("Enter 1st no.:"))
b = int(input("Enter 2nd no.:"))
print((str(bin(a ^ b))).count('1'))


