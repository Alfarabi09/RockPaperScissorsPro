class GameRules:
    @staticmethod
    def determine_winner(player_choice, computer_choice, moves):
        player_index = moves.index(player_choice)
        computer_index = moves.index(computer_choice)
        n = len(moves)
        half_n = n // 2
    
        if player_index == computer_index:
            return "Draw"
        elif (player_index < computer_index and computer_index - player_index <= half_n) or (player_index > computer_index and player_index - computer_index > half_n):
            return "Computer wins!"
        else:
            return "Player wins!"



