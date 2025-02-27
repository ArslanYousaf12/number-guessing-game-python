from art import logo
import random

print(logo)
print("Welcome to the Number Guessing Game ")

random_num = random.randint(1,100)
print(random_num)
remaining_attempts = 0
print("I am thinking of a number between 1 and 100 ")
diff_level = input("Choose the difficulty level Type easy or hard ")


if diff_level == "easy":
    remaining_attempts = 10
elif diff_level == "hard":
    remaining_attempts = 5
else:
    print("you enter invalid input ")

def compare_number(user_guess):

    if user_guess == random_num:
        return "You guess the right number you win "
    elif user_guess > random_num:
        return "Too high"
        
    elif user_guess < random_num:
        return "Too low"
        

while not  remaining_attempts == 0:
    print(f"You have {remaining_attempts} attempts remaining to guess the number ")
    guess = int(input("Make a guess "))
    remaining_attempts = remaining_attempts - 1
    compared_result = compare_number(guess)
    if compared_result == "You guess the right number you win ":
        print(compared_result)
        break
    else:
        print(compared_result)
    if not remaining_attempts == 0:
        print("Guess again")
    else:
        print("Game over ")
    





