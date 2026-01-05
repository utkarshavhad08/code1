import random

number = random.randint(1, 100)

guess_count = 0
guess = 0

print("Number Guessing Game")
print("Guess a number between 1 and 100")

while guess != number:
    guess = int(input("Enter your guess: "))
    guess_count += 1

    if guess > number:
        print("Too high")
    elif guess < number:
        print("Too low")
    else:
        print("Congratulations!")
        print("You guessed the number correctly.")
        print("Total guesses:", guess_count)