# imported random and used random.choice to choose between a random word in a list

import random

words = ["mosiah", "helaman", "nephi", "moroni"]

secret = random.choice(words)

print("Welcome to the word guessing game!")
print()

print("Your hint is: ", end="")

for i in range(len(secret)):
    print(f"_ ", end="")

print()

guess = ""
guess_count = 0

# This will only run when user guess isn't secret number
while guess != secret:
    guess = input("What is your guess? ").lower()

    # Shortcut of guess_count = guess_count + 1
    guess_count += 1

    if len(guess) != len(secret):
        print("Sorry, the guess must have the same number of letters as the secret word.")
        print()
    elif guess == secret:
        print("Congratulations! You guessed it!")
    else:
        print("Your hint is: ", end="")

        for i in range(len(guess)):
            if guess[i] == secret[i]:
                print(f"{guess[i].upper()} ", end="")
            elif guess[i] in secret:
                print(f"{guess[i].lower()} ", end="")
            else:
                print("_ ", end="")

        print() # new line

    # Word the sentence correctly
if guess_count == 1:
    print(f"It took you {guess_count} guess.")
else:
    print(f"It took you {guess_count} guesses.")

