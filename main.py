import sys
from game_logic import TableGenerator, GameRules
from utils import CryptoUtil, MoveValidator

def main():
    moves = sys.argv[1:]

    try:
        MoveValidator.validate_moves(moves)
    except ValueError as e:
        print(f"Error: {e}")
        print("Usage: python3 main.py <odd number of unique moves>")
        return
    
    while True:
        # 1. Generate computer move and HMAC before user input
        key = CryptoUtil.generate_key()
        computer_move = moves[CryptoUtil.generate_key()[0] % len(moves)]
        hmac_value = CryptoUtil.compute_hmac(computer_move, key)
        
        print("Available moves:")
        for i, move in enumerate(moves):
            print(f"{i + 1} - {move}")
        print("0 - exit")
        print("? - help")
        print(f"HMAC: {hmac_value}")

        choice = input("Enter your move: ")
        if choice == "0":
            print("Exiting the game.")
            return
        if choice == "?":
            TableGenerator.print_table(moves)
            continue

        try:
            player_move_index = int(choice) - 1
            player_move = moves[player_move_index]
        except (ValueError, IndexError):
            print("Invalid choice. Try again.")
            continue

        # 2. Display moves and result after user input
        print(f"Your move: {player_move}")
        print(f"Computer move: {computer_move}")

        winner = GameRules.determine_winner(player_move, computer_move, moves)

        if winner == "Draw":
            print("It's a draw!")
        elif winner == "Player wins!":
            print("You win!")
        elif winner == "Computer wins!":
            print("Computer wins!")

        # 3. Display the HMAC key for verification after displaying the result
        print(f"HMAC key: {key.hex()}\n")

if __name__ == "__main__":
    main()