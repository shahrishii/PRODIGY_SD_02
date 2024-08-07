import random

def guess_the_number():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed_correctly = False
    
    print("Welcome to the Guess the Number game!")
    print("I'm thinking of a number between 1 and 100.")
    
    while not guessed_correctly:
        try:
            # Get the user's guess
            user_guess = int(input("Enter your guess: "))
            attempts += 1
            
            # Compare the user's guess to the generated number
            if user_guess < number_to_guess:
                print("Too low! Try again.")
            elif user_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                guessed_correctly = True
                print(f"Congratulations! You've guessed the number {number_to_guess}.")
                print(f"It took you {attempts} attempts to guess correctly.")
        except ValueError:
            print("Please enter a valid integer.")

# Run the game
if __name__ == "__main__":
    guess_the_number()
