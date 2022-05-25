print('''Program to determine no. of candies in the bowl given that:\n
1. On dividing candies evenly among 5 people, the amount leftover is 2.
2. On dividing candies evenly among 6 people, the amount leftover is 3.
3. On dividing candies evenly among 7 people, the amount leftover is 2.\n\n''')

for candies in range(0, 200):
    if ((candies % 5) == 2) & ((candies % 6) == 3) & ((candies % 7) == 2):
        print(f"Number of candies in the jar is {candies}.")