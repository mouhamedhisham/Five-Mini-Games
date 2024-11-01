import os
import random
import numpy as np

LEADERBOARD_FILE = "tic_tac_toe_leaderboard.txt"

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

def display_leaderboard():
    leaderboard = load_leaderboard()
    print("\nLeaderboard:")
    if leaderboard:
        for i, (name, score) in enumerate(leaderboard.items(), 1):
            print(f"{i}. {name}: {score}")
    else:
        print("No players on the leaderboard yet.")
    print()

def reset_game():
    print("----------------------------------------------------")
    xo = np.array([str(i) for i in range(1, 10)])
    my_turn = random.choice([True, False])

    if my_turn:
        my_symbol = "X"
        pc_symbol = "O"
    else:
        my_symbol = "O"
        pc_symbol = "X"

    return xo, my_symbol, pc_symbol, my_turn

def update_board(xo, position, symbol):
    index = position - 1
    xo[index] = symbol

def get_pc_move(xo):
    available_positions = [i for i in range(1, 10) if xo[i - 1] not in ["X", "O"]]
    return random.choice(available_positions)

def print_tic_tac_toe_board(array):
    print(f" {array[0]} | {array[1]} | {array[2]} ")
    print("---|---|---")
    print(f" {array[3]} | {array[4]} | {array[5]} ")
    print("---|---|---")
    print(f" {array[6]} | {array[7]} | {array[8]} ")

def get_valid_position(xo):
    while True:
        try:
            position = int(input("Enter a position between 1 and 9: "))
            if 1 <= position <= 9:
                if xo[position - 1] in [str(i) for i in range(1, 10)]:
                    return position
                else:
                    print("Position already taken. Please select another position.")
            else:
                print("Invalid position. Please enter a number between 1 and 9.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def check_game_status(xo, my_symbol):
    # Diagonal check
    if (xo[0] == xo[4] == xo[8] and xo[0] in ["X", "O"]) or (xo[2] == xo[4] == xo[6] and xo[2] in ["X", "O"]):
        winner = xo[0] if xo[0] in ["X", "O"] else xo[2]
        print("You Won!" if winner == my_symbol else "PC Won!")
        return winner == my_symbol

    # Horizontal check
    for i in range(0, 9, 3):
        if xo[i] == xo[i+1] == xo[i+2] and xo[i] in ["X", "O"]:
            winner = xo[i]
            print("You Won!" if winner == my_symbol else "PC Won!")
            return winner == my_symbol

    # Vertical check
    for i in range(3):
        if xo[i] == xo[i + 3] == xo[i + 6] and xo[i] in ["X", "O"]:
            winner = xo[i]
            print("You Won!" if winner == my_symbol else "PC Won!")
            return winner == my_symbol

    # Check for draw
    if all(pos in ["X", "O"] for pos in xo):
        print("It's a draw!")
        return None  # Indicate a draw

    return False

def play_tic_tac_toe():
    player_name = input("Enter your name: ")
    leaderboard = load_leaderboard()

    xo, my_symbol, pc_symbol, my_turn = reset_game()

    while True:
        print_tic_tac_toe_board(xo)

        if my_turn:
            print(f"Enter number to place {my_symbol}")
            player_tile_position = get_valid_position(xo)
            update_board(xo, player_tile_position, my_symbol)
            if check_game_status(xo, my_symbol):
                update_leaderboard(player_name, 1, leaderboard)  # Update player score if they win
                break  # Exit the loop once the game is over
        else:
            print("PC is making a move...")
            pc_tile_position = get_pc_move(xo)
            update_board(xo, pc_tile_position, pc_symbol)
            if check_game_status(xo, my_symbol) is not False:
                break  # Exit the loop once the game is over

        # Toggle turn
        my_turn = not my_turn

    return game_end_options()

def game_end_options():
    while True:
        print("1) Play again")
        print("2) Main menu")
        print("3) View leaderboard")
        try:
            option = int(input("Enter your choice: "))
            if option == 1:
                return True  # Play again
            elif option == 2:
                return False  # Go back to menu
            elif option == 3:
                display_leaderboard()
            else:
                print("Invalid option. Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")
