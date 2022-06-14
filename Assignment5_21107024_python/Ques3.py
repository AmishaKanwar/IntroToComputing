import math
a = float(input("Enter the length of 1st side of a triangle:"))
b = float(input("Enter the length of 2nd side of a triangle:"))
c = float(input("Enter the length of 3rd side of a triangle:"))
# Checking the condition for the existence of the triangle
end_result = (a>=(b+c)) | (b>=(a+c)) | (c>=(a+b)) == 1
print(f"Can a triangle be formed with sides {a}, {b} and {c} units?", str(end_result).replace('True', 'No').replace('False', 'Yes'), sep = "\n")

# Calculating the area of the triangle if the condition is satisfied
if end_result == False:
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c)) 
    print(f"The area of the triangle with the sides {a}, {b} and {c} units is {area} sq. units.")