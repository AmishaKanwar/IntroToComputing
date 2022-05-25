import random
print("MULTIPLICATION GAME FOR KIDS [Solve 10 randomly generated questions] :)")
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

ch = 'y'
while ch == 'y':
    i = 1
    while i <= 10:
        num1 = random.choice(a)
        num2 = random.choice(a)
        answer = int(input(f"Question {i}: {num1} x {num2} = "))
        if answer == (num1 * num2):
            print("Right!")
        else:
            print(f"Wrong. The answer is {num1 * num2}.")
        i += 1
    ch = input("Do you want to play again? [Press 'y' for yes and any other key to exit.]")
