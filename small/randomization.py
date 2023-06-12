# Generate a random number between 1 and 9 (including 1 and 9).
# Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.

import random

# loop in bool statement
while True:
    num = random.randint(1, 10)

    user_guess = int(input("Guess a number: "))
    print("\n" + "System Generated: " + str(num))
    print("Your Input: " + str(user_guess))
    print("")

    # condtions or rules
    if user_guess == num:
        print("Hurrey!!! You won!")
        break
    elif user_guess < num:
        print("Oops! You guessed too low.")
    else:
        print("Oops!! You guessed too high.")
    print("")