# imports
from random import randint

# interface class
class Interface:
    def display_main_menu(self):
        print("+--------------------------------+")
        print("|    Rock, Paper and Scissors    |")
        print("+--------------------------------+")
        print("|                                |")
        print("| 1. PvP                         |")
        print("| 2. PvE                         |")
        print("| 3. Exit                        |")
        print("|                                |")
        print("+--------------------------------+")

    def display_round_menu(self):
        print("+--------------------------------+")
        print("|    Rock, Paper and Scissors    |")
        print("+--------------------------------+")
        print("|                                |")
        print("| 1. OneShot                     |")
        print("| 2. 3 Rounds                    |")
        print("| 3. Exit                        |")
        print("|                                |")
        print("+--------------------------------+")

    def display_game_options(self, score, turn):
        print("+--------------------------------+")
        print(f"|   PLAYER 1: {score[0]} | PLAYER 2: {score[1]}    |")
        print("+--------------------------------+")
        print(f"|        {turn} TURN           |")
        print("+--------------------------------+")
        print("|                                |")
        print("| 1. Rock                        |")
        print("| 2. Paper                       |")
        print("| 3. Scissors                    |")
        print("|                                |")
        print("+--------------------------------+")

    def compare_players(self, selection, score):
        print("+--------------------------------+")
        print(f"|   PLAYER 1: {score[0]} | PLAYER 2: {score[1]}    |")
        print("+--------------------------------+")
        print(f"        {str(selection[0]).upper()} VS {str(selection[1]).upper()}            ")
        print("+--------------------------------+")

# check both selections and verify who won
def get_winner(player1, player2):
    # a dict with a win condition
    win_condition = {
        "rock": "scissors",
        "scissors": "paper",
        "paper": "rock"
    }

    # drawn logic
    if player1 == player2:
        return "Drawn!"

    # we gonna verify the winner with the player 1 as base
    # # When we look up a move in the dictionary, such as "rock", it returns the move it defeats, in this case "scissors". 
    if win_condition[player1] == player2:
        return "Player 1 win!"
    else:
        return "Player 2 win!"

# just space
def space():
    print("\n"*30)

# instancing interface class
interface = Interface()
while True:
    # oponnent choice block
    while True:
        space()
        interface.display_main_menu()
        print()

        # option select block
        try:
            option = int(input(" +- Choose your oponnent: "))
            # if the option is invalid (a not integer, more then 3 or less then 3) raises ValueError except
            if option > 3 or option < 1:
                raise ValueError

            break
        # After press enter go back to the start
        except ValueError:
            print()
            print("+--------------------------------+")
            print("| Please select an valid option  |")
            print("+--------------------------------+")
            print()
            input("...")

    # exit option
    if option == 3:
        break

    if option == 1:
        mode = "pvp"
        turn = True
    else:
        mode = "pve"
        turn = None

    # mode choice block
    while True:
        space()
        interface.display_round_menu()
        print()

        # option select block
        try:
            option = int(input(" +- Choose your mode: "))
            # if the option is invalid (a not integer, more then 3 or less then 3) raises ValueError except
            if option > 3 or option < 1:
                raise ValueError

            break
        # After press enter go back to the start
        except ValueError:
            print()
            print("+--------------------------------+")
            print("| Please select an valid option  |")
            print("+--------------------------------+")
            print()
            input("...")

    # exit option
    if option == 3:
        break

    rounds = 3 if option == 2 else 0

    game = True
    player1_score = 0
    player2_score = 0
    while game:
        player1_selection = ""
        player2_selection = ""
        
        # if the pve mode is on everytime that we display the "game_options" will be "PLAYER 1"
        player_time = "PLAYER 1"

        option_list = ["rock", "paper", "scissors"]
        if mode == "pve":
            player2_selection = option_list[randint(0, len(option_list)-1)]    

        while True:
            # here is basically saying, if the pve mode is off we gonna change the player time
            if turn != None:
                player_time = "PLAYER 1" if turn == True else "PLAYER 2"
            
            space()
            interface.display_game_options([player1_score, player2_score], player_time)
            print()
            
            # player selection block
            try:
                option = int(input(" +- Select your option: "))
                # we gonna utilize the option list that we create before
                # if the option is between 1 and 3 it gonna accept it, if out of it, raise value error
                if option > 0 and option < 4:
                    if turn == False:
                        player2_selection = option_list[option-1]
                    else:
                        player1_selection = option_list[option-1]
                else:
                    raise ValueError

                if turn != None:
                    turn = not turn
            # After press enter go back to the start
            except ValueError:
                print()
                print("+--------------------------------+")
                print("| Please select an valid option  |")
                print("+--------------------------------+")
                print()
                input("...")

            # if both players selections arent empty break the loop and keep going
            if player2_selection != "" and player1_selection != "":
                 break

        winner = get_winner(player1_selection, player2_selection)
        # score logic
        if winner == "Player 1 win!":
            player1_score += 1
        elif winner == "Player 2 win!":
            player2_score += 1

        space()
        interface.compare_players([player1_selection, player2_selection], [player1_score, player2_score])
        print()
        
        print(f" +- {winner}")
        print()
        input("...")

        # Drawn dont count as a round
        rounds -= 1 if winner != "Drawn!" else 0

        # the game will finish if the round hits 0 or the player score hits 2
        if winner != "Drawn!" and (rounds <= 0 or player1_score >= 2 or player2_score >= 2):
            break