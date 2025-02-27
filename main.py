from art import logo
import random

# Print the game logo
print(logo)
print("Welcome to the Number Guessing Game ")

# Generate a random number between 1 and 100
random_num = random.randint(1, 100)
print(random_num)  # For debugging purposes, print the random number
remaining_attempts = 0
print("I am thinking of a number between 1 and 100 ")

# Ask the user to choose a difficulty level
diff_level = input("Choose the difficulty level. Type 'easy' or 'hard': ")

# Set the number of attempts based on the chosen difficulty level
if diff_level == "easy":
    remaining_attempts = 10
elif diff_level == "hard":
    remaining_attempts = 5
else:
    print("You entered an invalid input")

# Function to compare the user's guess with the random number
def compare_number(user_guess):
    if user_guess == random_num:
        return "You guessed the right number! You win!"
    elif user_guess > random_num:
        return "Too high"
    elif user_guess < random_num:
        return "Too low"

# Loop until the user runs out of attempts
while remaining_attempts != 0:
    print(f"You have {remaining_attempts} attempts remaining to guess the number")
    guess = int(input("Make a guess: "))
    remaining_attempts -= 1  # Decrease the number of attempts by 1
    compared_result = compare_number(guess)
    
    if compared_result == "You guessed the right number! You win!":
        print(compared_result)
        break  # Exit the loop if the user guessed the correct number
    else:
        print(compared_result)
    
    if remaining_attempts != 0:
        print("Guess again")
    else:
        print("Game over")