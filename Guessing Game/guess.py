import random

# Generate a random number between 1 and 10
hidden_number = random.randint(1, 10)

# Initialize the number of chances
chances = 3

# Loop through the chances
for i in range(chances):
    # Ask the user for input
    guess = int(input("Guess the number (between 1 and 10): "))
    
    # Check if the guess is correct
    if guess == hidden_number:
        print("Congratulations! You guessed the number correctly.")
        break
    else:
        # Provide a hint
        if guess < hidden_number:
            print("Try again. The number is higher.")
        else:
            print("Try again. The number is lower.")
else:
    # If the loop completes without a correct guess
    print("Sorry, you ran out of chances. The number was", hidden_number)
