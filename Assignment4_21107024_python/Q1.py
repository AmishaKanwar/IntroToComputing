ch = 'y'
while ch == 'y':
    marks = float(input("Enter your marks: "))
    if marks < 25:
        print("Your grade is F.")
    elif (marks >= 25) & (marks < 45):
        print("Your grade is E.")
    elif (marks >= 45) & (marks < 50):
        print("Your grade is D.")
    elif (marks >= 50) & (marks < 60):
        print("Your grade is C.")
    elif (marks >= 60) & (marks < 80):
        print("Your grade is B.")
    elif (marks >= 80) & (marks <= 100):
        print("Your grade is A.")
    else:
        print("Invalid Input (Marks should be less than or equal to 100.)")
    
    ch = input("Do you want to continue? (Enter y for yes and n (or any key other than y) for no)")
    
