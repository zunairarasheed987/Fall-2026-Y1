import random

secret_number = random.randint(1, 100)
MAX_ATTEMPTS = 7
attempts = 0
guessed = False

print("Guess the secret number between 1 and 100.")
print(f"You have {MAX_ATTEMPTS} attempts.\n")

while attempts < MAX_ATTEMPTS:
    try:
        guess = int(input("Enter your guess: "))
    except ValueError:
        print("Invalid input! Please enter a number.\n")
        continue

    if guess < 1 or guess > 100:
        print("Guess must be between 1 and 100. This attempt is not counted.\n")
        continue

    attempts += 1

    if guess == secret_number:
        guessed = True
        if attempts == 1:
            print("Perfect score! You guessed it on the first attempt!")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
        break
    elif guess < secret_number:
        print(f"Too low! Attempts left: {MAX_ATTEMPTS - attempts}\n")
    else:
        print(f"Too high! Attempts left: {MAX_ATTEMPTS - attempts}\n")

if not guessed:
    print(f"Game over! The secret number was {secret_number}.")
