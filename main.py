from art import logo
import random

def initialize_game():
    """Initialize the game settings and return the target number"""
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100")
    return random.randint(1, 100)

def get_difficulty():
    """Get difficulty level from user and return number of attempts"""
    difficulty = input("Choose difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == "easy":
        return 10
    elif difficulty == "hard":
        return 5
    else:
        print("Invalid input. Defaulting to hard mode.")
        return 5

def check_guess(guess, target):
    """Compare guess with target number and return appropriate message"""
    if guess == target:
        return "You guessed the right number! You win!"
    return "Too high" if guess > target else "Too low"

def play_game():
    """Main game loop"""
    target_number = initialize_game()
    attempts = get_difficulty()
    
    while attempts > 0:
        print(f"\nYou have {attempts} attempts remaining to guess the number")
        
        try:
            guess = int(input("Make a guess: "))
            result = check_guess(guess, target_number)
            print(result)
            
            if result == "You guessed the right number! You win!":
                return
            
            attempts -= 1
            if attempts > 0:
                print("Guess again")
        except ValueError:
            print("Please enter a valid number!")
            continue
    
    print("\nGame Over! You've run out of attempts")
    print(f"The number was {target_number}")

if __name__ == "__main__":
    play_game()