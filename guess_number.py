import os
import random

LEADERBOARD_FILE = "guess_number_leaderboard.txt"

def load_leaderboard():
    leaderboard = {}
    if os.path.exists(LEADERBOARD_FILE):
        with open(LEADERBOARD_FILE, "r") as file:
            for line in file:
                name, score = line.strip().split(":")
                leaderboard[name] = int(score)
    return leaderboard

def save_leaderboard(leaderboard):
    sorted_leaderboard = dict(sorted(leaderboard.items(), key=lambda item: item[1], reverse=True))

    with open(LEADERBOARD_FILE, "w") as file:
        for name, score in sorted_leaderboard.items():
            file.write(f"{name}:{score}\n")


def update_leaderboard(player_name, score, leaderboard):
    if player_name in leaderboard:
        leaderboard[player_name] += score
    else:
        leaderboard[player_name] = score
    save_leaderboard(leaderboard)
    

def play_Number_Guessing_Game():
    print("How to play:")
    print("You have 3 guesses only.")
    print("If you guess correctly on the first try, you get 3 points.")
    print("On the second try, you get 2 points.")
    print("On the third try, you get 1 point.")
    
    
    player_name = input("Enter your name: ")

    leaderboard = load_leaderboard()

    if player_name in leaderboard:
        print(f"Welcome back, {player_name}! Your current score is {leaderboard[player_name]}.")
    else:
        print(f"Hello, {player_name}! This is your first time playing.")
    
    
    score = 0
    attempts = 3
    
    random_number = random.randint(0, 10)
    
    while attempts > 0:
        guessed_number= None
        while guessed_number is None:
            try:
                guessed_number = int(input(f"Guess a number between 0 and 10 (You have {attempts} guesses left): "))
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        if guessed_number == random_number:
            print("Congratulations, you guessed the correct number!")
            score = attempts
            break
        elif guessed_number > random_number:
            print("Lower!")
        else:
            print("Higher!")
        
        attempts -= 1

    if score > 0:
        print(f"Your score = {score}")
        update_leaderboard(player_name, score, leaderboard)
    else:
        print(f"Sorry, you lost! The correct number was {random_number}.")
        print("Your score = 0")
        update_leaderboard(player_name, score, leaderboard)
    
    return game_end_options()   
        
# Function to display game end options with input validation
def game_end_options():
    while True:
        print("1) Play again")
        print("2) Main menu")
        try:
            option = int(input("Enter your choice: "))
            if option == 1:
                return True  # Play again
            elif option == 2:
                return False  # Go back to menu
            else:
                print("Invalid option. Please enter 1 or 2.")
        except ValueError:
            print("Invalid input. Please enter a number (1 or 2).")
        