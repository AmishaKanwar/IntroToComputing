# Question 1
#Taking input from the user (3 numbers)
num1 = float(input("Enter 1st number:"))
num2 = float(input("Enter 2nd number:"))
num3 = float(input("Enter 3rd number:"))
avg = (num1 + num2 + num3)/3   # Computing average using arithmetic operators
print("The average of the three numbers is", avg, end = '\n_____________________________\n')


# Question 2
# Python program to compute a person's income tax
gross_income = float(input("Enter gross income (in $):"))
num_dependents = int(input("Enter no. of dependents:"))
std_deduction = 10000
tax_rate = 0.2
dependent_deduct = 3000
# round() is used to round off the gross income to the nearest penny
taxable_income = (round(gross_income, 2)) - std_deduction - (dependent_deduct * num_dependents)
tax = taxable_income * tax_rate
print("Income Tax (in $):", tax, end = '\n_____________________________\n')


# Question 3
TotalSeconds = int(input("Enter number of seconds:"))
# Aritmetic operators used to convert the input of total seconds from the user to minutes and seconds
min = TotalSeconds // 60
sec = TotalSeconds % 60
print(TotalSeconds, "seconds =", min, "minutes", sec, "seconds", end = '\n_____________________________\n')


# Question 4
number1 = 25
number2 = '25'
number3 = 25.0
# Using str() to convert the resultant integer value into string
sum = str(number1 + int(number2) + int(number3))
print(sum, type(sum), sep = '\n', end = '\n_____________________________\n')


# Question 5
import math
# for loop utilised to print the required output
for i in range(0, 346, 15):
  print(i, "---", round(math.sin(math.radians(i)), 4), round(math.cos(math.radians(i)), 4))