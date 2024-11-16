import sys
import random
from enum import Enum

def rps(name="player"):
    game_count = 0
    player_wins = 0
    python_wins = 0

    def play_rps():
        nonlocal name
        nonlocal player_wins
        nonlocal python_wins

        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        player_choice = input(f"\n{name}, Enter... \n1 for Rock \n2 for Paper\n3 for scissors\n\nop: ")

        if player_choice not in ["1", "2", "3"]:
            print("Bad option")
            return play_rps()
        
        player = int(player_choice)

        computer_choice = random.choice("123")
        computer = int(computer_choice)

        print(f"\nYou chose {str(RPS(player)).replace("RPS.", "").title()}.")
        print(f"Python chose {str(RPS(computer)).replace("RPS.", "").title()}.\n")

        def decide_winner(player, computer):
            nonlocal name
            nonlocal player_wins
            nonlocal python_wins

            if player == 1 and computer == 3:
                player_wins += 1
                return f"{name} win! :D"
            elif player == 2 and computer == 1:
                player_wins += 1
                return f"{name} win! :D"
            elif player == 3 and computer == 2:
                player_wins += 1
                return f"{name} win! :D"
            elif player == computer:
                return "Tie game!"
            else:
                python_wins += 1
                return "Python win! D:"
        
        game_result = decide_winner(player, computer)

        print(game_result)

        nonlocal game_count
        game_count += 1

        print(f"\nGame count: {game_count}")
        print(f"\nPlayer wins: {player_wins}")
        print(f"\nPython wins: {python_wins}")

        print("\nPlay again?")

        while True:
            play_again = input("\nY for yes or \nQ to quit\n")

            if play_again.lower() not in ["y", "q"]:
                continue
            else:
                break
        
        if play_again.lower() == "y":
            return play_rps()
        else:
            print("\nByeee!!!\n")
            sys.exit("xd")
    
    return play_rps



if __name__ == "__main__":
    import argparse
    # Creamos el objeto encargado de procesar los argumentos
    parser = argparse.ArgumentParser(description="Personalize game experience.")

    # Creamos un argumento flag
    parser.add_argument(
        "-n", 
        "--name", 
        metavar="name",     
        required=True,      
        help="the name of the player"
    )

    # Recibimos los argumentos
    args = parser.parse_args()

    rock_paper_scissors = rps(args.name)
    rock_paper_scissors()