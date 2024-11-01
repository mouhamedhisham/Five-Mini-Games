import random
import os
global score 

LEADERBOARD_FILE = "hangMan_leaderboard.txt"
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

def choose_randomWord(list):
    random_word = str(random.choice(list))
    random_word=random_word.lower()
    return random_word
    
def draw(step):
    if step == 1:
        print("     ---------")
    elif step == 2: 
        print("          |")
        print("          |")
        print("          |")
        print("          |")
        print("          |")
        print("          |")
        print("     ----------")
    elif step == 3:
        print("   ---------")
        print("            |")
        print("            |")
        print("            |")
        print("            |")
        print("            |")
        print("            |")
        print("       ----------")
       
    elif step == 4:
        print("   ---------")
        print("  |         |")
        print("            |")
        print("            |")
        print("            |")
        print("            |")
        print("            |")
        print("       ----------")
    elif step == 5:
        print("   ---------")
        print("  |         |")
        print("  O         |")
        print("            |")
        print("            |")
        print("            |")
        print("            |")
        print("       ----------")
    elif step == 6:
        print("  ----------")
        print("  |         |")
        print("  O         |")
        print(" /|\        |")
        print("            |")
        print("            |")
        print("            |")
        print("       ----------")
    elif step == 7:
        print("  ----------")
        print("  |         |")
        print("  O         |")
        print(" /|\        |")
        print(" / \        |")
        print("            |")
        print("            |")
        print("       ----------")
        
def play(words_list,player_name,leaderboard):
    steps = 0
    score = 7

    random_word = list(choose_randomWord(words_list))
    
    hidden_word = ['*' for i in range(len(random_word))]
                
    while hidden_word != random_word and steps < 7: 
        word = ''.join(hidden_word)
        print(word)
        input_char = input("choose a letter: ")
        if input_char in random_word:
            for ind,char in enumerate(random_word):
                if char == input_char:                            
                    hidden_word[ind] = input_char
                            
        else:
            score -= 1
            steps += 1  
            draw(steps)
            if steps == 7:
                print("You lost! The word was:", ''.join(random_word))
               
    if steps != 7:
        print(f"You won the game and your score is {score}") 
    update_leaderboard(player_name, score, leaderboard)
    
        
def game_end_options():
    while True:
        print("1) Play again")
        print("2) Main menu")
        try:
            option = int(input("Enter your choice: "))
            if option == 1:
                
                return True
            elif option == 2:
                
                return False  # Go back to menu
            else:
                print("Invalid option. Please enter 1 or 2.")
        except ValueError:
            print("Invalid input. Please enter a number (1 or 2).")       
                                  
def hangMan_game():
    flag = True
    while flag:
        print("-"*30)
        print("Welcome to the handMan Game!")
        print("How to play:")
        print("You have 7 guesses only.")
        print("If you guess correctly on the first try, you get 7 points.")
        print("On the second try, you get 6 points and so on.....")
        print("-"*30)
       
        try:
            player_name = input("Enter your name: ")
            leaderboard = load_leaderboard()
            if player_name in leaderboard:
                print(f"Welcome back, {player_name}! Your current score is {leaderboard[player_name]}.")
            else:
                print(f"Hello, {player_name}! This is your first time playing.")

            print("(1)- Easy")
            print("(2)- Medium")
            print("(3)- Hard")
            n = int(input("Choose difficulty (1, 2, 3): "))

            if n == 1:
                with open(r"C:\Five-mingame\EasyWords.txt", 'r') as file:  # Use raw string for Windows paths
                    lines = file.readlines()
                
                words_list = [line.strip() for line in lines]
                play(words_list,player_name,leaderboard)    

                                
            elif n == 2:
                with open(r"C:\Five-mingame\MediumWords.txt", 'r') as file:
                    lines = file.readlines()
                word_lists = [line.strip() for line in lines]
                play(word_lists,player_name,leaderboard)
                

            elif n == 3:
                with open(r"C:\Five-mingame\HardWords.txt", 'r') as file:
                    lines = file.readlines()
                word_lists = [line.strip() for line in lines]
                play(word_lists,player_name,leaderboard)
                
            else:
                print("Invalid choice. Please enter 1, 2, 3.")
            
            flag = game_end_options()

        except ValueError:
            print("That's not a valid number. Please try again.")
        except FileNotFoundError as e:
            print(f"Error: {e}")