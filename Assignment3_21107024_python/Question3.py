import math

#Expression 1
print("Calculating the value of the expression (3 + 4) * 5")
exp_1 = (3 + 4) * 5
print("Value", exp_1, end = '\n\n')

#Expression 2 
print("Calculating the value of the expression (n * (n - 1)) / 2")
n = float(input("Enter a real number, n: "))
exp_2 = (n * (n - 1)) / 2
print(f"Value of the given expression is {exp_2}", end = '\n\n')

#Expression 3
print("Calculating the area of the circle (4*pi*(r**2)) with the radius, r")
r = float(input("Enter radius: "))
area = 4 * math.pi * (r**2)
print(f"Area of the circle is {area} sq. units.", end = '\n\n')

#Expression 4
print("Calculating the value of the square root of the expression (r*(cos(a)**2)) + (r*(sin(b)**2))")
print(f'r = radius = {r} (input taken before)')
a = float(input("Enter the value of angle a (in radians): "))
b = float(input("Enter the value of angle b (in radians): "))
exp_4 = math.sqrt((r * (math.cos(a) ** 2)) + (r * (math.sin(b) ** 2)))  #a and b are in radians
print('Value of the given expression: ', exp_4, end = '\n\n')

#Expression 5
print("Calculating slope of the line ((y2-y1)/(x2-x1)) using the coordinates of 2 points on the line")
x1 = float(input("Enter the abscissa of the 1st point (x1): "))
y1 = float(input("Enter the ordinate of the 1st point (y1): "))
x2 = float(input("Enter the abscissa of the 2nd point (x2): "))
y2 = float(input("Enter the ordinate of the 2nd point (y2): "))
slope = (y2 - y1)/(x2 - x1)
print(f"The slope is {slope}.")