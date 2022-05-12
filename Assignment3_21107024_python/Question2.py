#Interactive Python Calculator Program
print("Calculator at your service :)")
num1 = float(input("Enter first operand (number): "))
num2 = float(input("Enter second operand (number): "))
print("Press the following keys for the required operations:\
    \n1 for addition\
    \n2 for subtraction\
    \n3 for multiplication\
    \n4 for division\
    \n5 for calculating remainder\
    \n6 for calculating quotient(floor division)\
    \n7 for raising the first number to the second number (exponentiation)")

ch = 'y'
while ch == 'y':
    i = input("Press the key for the required operation to be undertaken: ")
    if i == '1':
        print(f"Sum = {num1 + num2}.")
    elif i =='2':
        print(f"Difference = {num1 - num2}.")
    elif i == '3':
        print(f"Product = {num1 * num2}")
    elif i == '4':
        print(f"{num1}/{num2} = {num1 / num2}")
    elif i == '5':
        print(f"Remainder = {num1 % num2}")
    elif i == '6':
        print(f"Quotient (obtained from floor division) = {num1 // num2}")
    elif i == '7':
        print(f"Resultant of the exponentiation ({num1}**{num2}) = {num1 ** num2}")
    else:
        print("Invalid operation")
    ch = input("Do you want to continue? (Press y for yes and n for no)")
