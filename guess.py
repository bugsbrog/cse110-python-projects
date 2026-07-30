import random

# Without this, the terminal will give error
keep_playing = "yes"

while keep_playing == "yes":
    secret_number = random.randint(1, 100)

    guess_count = 0
    guess = -1

# This will only run when user guess isn't secret number
    while guess != secret_number:
        guess = int(input("What is your guess? "))

        # Shortcut of guess_count = guess_count + 1
        guess_count += 1

        if guess < secret_number:
            print("Higher")
        elif guess > secret_number:
            print("Lower")
        else:
            print("You guessed it!")

    # Word the sentence correctly
    if guess_count == 1:
        print(f"It took you {guess_count} guess")
    else:
        print(f"It took you {guess_count} guesses")

    keep_playing = input("Would you like to play again (yes/no)? ")

else:
    print("Thank you for playing. Goodbye.")